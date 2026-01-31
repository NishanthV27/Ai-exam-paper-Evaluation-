# 📘 AI Powered Exam Paper Evaluation System

## 📌 Project Overview

The **AI Powered Exam Paper Evaluation System** is a web-based application that automatically evaluates student answer sheets using Artificial Intelligence and Machine Learning techniques.

The system allows users (teacher/admin) to upload:
- Question paper (PDF or Image)
- Student answer sheet (PDF or Image)

Using **OCR (Optical Character Recognition)**, the system extracts text from the uploaded files.  
An AI model generates correct answers for each question and compares them with student answers using **semantic similarity**.  
Based on the similarity score, marks and grades are calculated automatically.

This project reduces manual correction time and improves accuracy in exam evaluation.

---

## 🎯 Objectives

- Automate the exam paper evaluation process  
- Reduce manual effort of teachers  
- Improve accuracy and speed of correction  
- Apply AI and Machine Learning in education  
- Generate and store results digitally  

---

## ⚙️ Features

- Upload question paper and student answer sheet (PDF/Image)  
- Extract text using OCR (Tesseract & PyPDF2)  
- Generate correct answers using AI (GPT4All)  
- Compare answers using Sentence Transformer (ML model)  
- Automatic marks and grade calculation  
- Store results in SQLite database  
- View results in dashboard  
- Download results as PDF  
- Simple web interface using Flask  

---

## 🛠️ Technologies Used

### 🔹 Backend
- Python  
- Flask  

### 🔹 Frontend
- HTML  
- CSS  

### 🔹 AI / Machine Learning
- SentenceTransformer (all-mpnet-base-v2)  
- GPT4All  

### 🔹 OCR & File Handling
- Pytesseract  
- PyPDF2  
- PIL (Pillow)  

### 🔹 Database
- SQLite  

### 🔹 Other Libraries
- FPDF  
- Regex  
- OS  

---

## 🔄 System Workflow

1. User uploads:
   - Question paper  
   - Student answer sheet  
2. System extracts text using OCR  
3. AI generates correct answers for each question  
4. Student answers are compared with correct answers  
5. Similarity score is converted into marks  
6. Grade is calculated  
7. Result is saved in database  
8. User can view and download result  

---

## 🧩 Project Structure

AI-Exam-Evaluation-System/
│
├── app.py
├── exam.db
├── uploads/
├── templates/
│ ├── upload_questions.html
│ ├── result.html
│ └── dashboard.html
├── static/
│ └── style.css
├── README.md
└── requirements.txt


---

## ▶️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/ai-exam-evaluation-system.git
cd ai-exam-evaluation-system
Step 2: Create Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate
Step 3: Install Required Libraries
pip install -r requirements.txt
Step 4: Run the Application
python app.py
Step 5: Open in Browser
http://127.0.0.1:5000/
📋 Requirements
Create a requirements.txt file with:

flask
pytesseract
pillow
PyPDF2
sentence-transformers
gpt4all
fpdf
sqlite3
📊 Grading System
Marks (%)	Grade
90 – 100	A+
75 – 89	A
60 – 74	B
50 – 59	C
Below 50	Fail
🚀 Future Enhancements
Add user authentication (login system)

Support for multiple subjects

Improve accuracy using fine-tuned AI models

Add charts and analytics in dashboard

Deploy on cloud (AWS / Render / Heroku)

Mobile responsive UI

👨‍💻 Author
Nishanth
B.Tech AI & ML Student
AI and Full Stack Developer

