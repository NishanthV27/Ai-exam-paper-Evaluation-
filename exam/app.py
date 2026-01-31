from flask import Flask, render_template, request, send_file, session, redirect, url_for
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util
from gpt4all import GPT4All
from fpdf import FPDF
import re, os, sqlite3

app = Flask(__name__)
app.secret_key = '7f3008e2ccbea5794abbb992d13f35feacc682bc97cf53222083a2082b3def49'
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

semantic_model = SentenceTransformer("all-mpnet-base-v2")
llm = GPT4All("gpt4all-falcon-q4_0.gguf")

def init_db():
    conn = sqlite3.connect('exam.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY,
                    question_text TEXT,
                    correct_answer TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY,
                    reg_no TEXT,
                    name TEXT,
                    marks REAL,
                    grade TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

QUESTIONS = []
FINAL_RESULTS = []


# ---------- OCR ----------
def extract_text(file_path):
    text = ""
    if file_path.lower().endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    else:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
    return text.strip()


# ---------- CLEAN ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()


# ---------- GENERATE MODEL ANSWER ----------
def generate_model_answer(question):
    prompt = f"Give a short correct answer for this exam question:\n{question}\nAnswer:"
    return llm.generate(prompt, max_tokens=150)


# ---------- EVALUATE ----------
def evaluate_answer(model_answer, student_answer):
    model_emb = semantic_model.encode([model_answer], convert_to_tensor=True)
    student_emb = semantic_model.encode([student_answer], convert_to_tensor=True)
    similarity = util.cos_sim(student_emb, model_emb).item()
    return round(similarity * 100, 2)


# ---------- GRADE ----------
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


# ---------- PARSE ANSWERS ----------
def parse_answers(answer_text):
    answers = {}
    lines = answer_text.split('\n')
    for line in lines:
        match = re.match(r'Q(\d+):\s*(.*)', line.strip())
        if match:
            q_num = int(match.group(1))
            ans = match.group(2).strip()
            answers[q_num] = ans
    return answers


# ---------- UPLOAD AND EVALUATE ----------
@app.route("/", methods=["GET", "POST"])
def upload_questions():
    if request.method == "POST":
        question_file = request.files["question_file"]
        answer_file = request.files["answer_file"]
        name = request.form["name"]
        reg_no = request.form["reg_no"]

        # Save and extract question text
        q_path = os.path.join(UPLOAD_FOLDER, question_file.filename)
        question_file.save(q_path)
        question_text = extract_text(q_path)

        # Save and extract student answer text
        a_path = os.path.join(UPLOAD_FOLDER, answer_file.filename)
        answer_file.save(a_path)
        answer_text = extract_text(a_path)

        # Parse questions
        questions_list = [q.strip() for q in question_text.split("\n") if q.strip()]

        # Parse student answers
        student_answers = parse_answers(answer_text)

        # Generate AI correct answers and evaluate
        total_marks = 0
        for i, q in enumerate(questions_list):
            q_num = i + 1
            model_answer = generate_model_answer(q)
            student_answer = student_answers.get(q_num, "")
            marks = evaluate_answer(model_answer, student_answer)
            total_marks += marks

        avg_marks = round(total_marks / len(questions_list), 2)
        grade = calculate_grade(avg_marks)

        # Store result in DB
        conn = sqlite3.connect('exam.db')
        c = conn.cursor()
        c.execute('INSERT INTO results (reg_no, name, marks, grade) VALUES (?, ?, ?, ?)', (reg_no, name, avg_marks, grade))
        conn.commit()
        conn.close()

        results = [{
            "reg_no": reg_no,
            "name": name,
            "marks": avg_marks,
            "grade": grade
        }]

        session['results'] = results
        return redirect(url_for('show_results'))

    return render_template("upload_questions.html")


# ---------- SHOW RESULTS ----------
@app.route("/result")
def show_results():
    results = session.get('results', [])
    return render_template("result.html", results=results)


# ---------- STUDENT SUBMIT ----------
@app.route("/submit", methods=["POST"])
def submit_answers():
    name = request.form["name"]
    reg_no = request.form["reg_no"]

    total_marks = 0

    # Fetch questions and correct answers from DB
    conn = sqlite3.connect('exam.db')
    c = conn.cursor()
    c.execute('SELECT id, question_text, correct_answer FROM questions')
    questions = c.fetchall()
    conn.close()

    for q_id, q_text, correct_ans in questions:
        answer_text = request.form.get(f"answer_{q_id}", "")
        file = request.files.get(f"answer_{q_id}")

        if file and file.filename != "":
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            answer_text += " " + extract_text(path)

        marks = evaluate_answer(correct_ans, answer_text)
        total_marks += marks

    avg_marks = round(total_marks / len(questions), 2)
    grade = calculate_grade(avg_marks)

    # Store result in DB
    conn = sqlite3.connect('exam.db')
    c = conn.cursor()
    c.execute('INSERT INTO results (reg_no, name, marks, grade) VALUES (?, ?, ?, ?)', (reg_no, name, avg_marks, grade))
    conn.commit()
    conn.close()

    results = [{
        "reg_no": reg_no,
        "name": name,
        "marks": avg_marks,
        "grade": grade
    }]

    session['results'] = results
    return redirect(url_for('show_results'))


# ---------- DOWNLOAD PDF ----------
@app.route("/download_pdf")
def download_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Evaluation Results", ln=True, align="C")
    pdf.ln(10)

    for r in FINAL_RESULTS:
        pdf.cell(200, 10, f"Reg No: {r['reg_no']}", ln=True)
        pdf.cell(200, 10, f"Name: {r['name']}", ln=True)
        pdf.cell(200, 10, f"Marks: {r['marks']}", ln=True)
        pdf.cell(200, 10, f"Grade: {r['grade']}", ln=True)
        pdf.ln(5)

    pdf_path = "results.pdf"
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)


# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect('exam.db')
    c = conn.cursor()
    c.execute('SELECT reg_no, name, marks, grade FROM results')
    rows = c.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "reg_no": row[0],
            "name": row[1],
            "marks": row[2],
            "grade": row[3]
        })

    return render_template("dashboard.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
