🔹 Project Title

AI Powered Exam Paper Evaluation System using Flask and Machine Learning

🔹 Project Description (Simple English)

This project is an AI-based exam paper evaluation system that automatically checks student answer sheets and gives marks and grades.

The system allows the user (teacher/admin) to upload:

Question paper (PDF or Image)

Student answer sheet (PDF or Image)

Using OCR (Optical Character Recognition), the system extracts text from the uploaded files.
Then, an AI model generates correct answers for each question.
After that, the system compares the student’s answers with the AI-generated answers using semantic similarity (machine learning).

Based on similarity score:

Marks are calculated

Grade is generated (A+, A, B, C, Fail)

Result is stored in a database (SQLite)

Result can be viewed in dashboard and downloaded as PDF

This reduces manual correction time and makes evaluation faster and more accurate.

🔹 Features

Upload question paper and answer sheet (PDF/Image)

Extract text using OCR (Tesseract & PyPDF2)

Generate correct answers using AI (GPT4All)

Compare answers using Sentence Transformer (ML model)

Automatic marks and grade calculation

Store results in SQLite database

View results in dashboard

Download results as PDF

Simple web interface using Flask

🔹 Technologies Used

Frontend: HTML, CSS (templates)

Backend: Python Flask

Database: SQLite

OCR: Pytesseract, PyPDF2

AI / ML: SentenceTransformer, GPT4All

PDF Generation: FPDF

Libraries: PIL, regex, os

🔹 Workflow (How it works)

User uploads:

Question paper

Student answer sheet

System extracts text using OCR

AI generates correct answers for each question

Student answers are compared with correct answers

Similarity score is converted into marks

Grade is calculated

Result is saved in database

User can view and download result

🔹 Objective of the Project

The main objective of this project is:

To automate exam paper evaluation

To reduce manual work of teachers

To improve accuracy and speed of correction

To use AI and machine learning in education

🔹 Short Description (for Resume – 3 lines)

Developed an AI Powered Exam Paper Evaluation System using Flask, OCR, and Machine Learning.
The system automatically extracts answers from PDFs/images, evaluates them using semantic similarity, and generates marks and grades.
Results are stored in a database and can be viewed on a dashboard or downloaded as PDF.

If you want, I can give you next in:
✅ Very short 2–3 line description
✅ Problem statement
✅ Abstract
✅ Architecture diagram explanation
✅ Viva explanation in simple English

Just say which one you want:
1) Abstract
2) Problem Statement
3) Resume short description
4) Viva explanation
5) All

i want readme file for this

Super Nishanth 👍 I’ll give you a professional README.md file for your
👉 AI Powered Exam Paper Evaluation System

You can directly copy and paste this into your project as README.md.

📘 AI Powered Exam Paper Evaluation System
📌 Project Overview

The AI Powered Exam Paper Evaluation System is a web-based application that automatically evaluates student answer sheets using Artificial Intelligence and Machine Learning techniques.

The system allows users to upload:

Question paper (PDF or Image)

Student answer sheet (PDF or Image)

Using OCR (Optical Character Recognition), the system extracts text from the uploaded files.
An AI model generates correct answers for each question and compares them with student answers using semantic similarity.
Based on the similarity score, marks and grades are calculated automatically.

This project helps reduce manual correction time and improves accuracy in exam evaluation.

🎯 Objectives

Automate the process of exam paper evaluation

Reduce human effort and time in checking answer sheets

Provide fast and accurate grading using AI

Store and manage student results in a database

Generate result reports in PDF format

⚙️ Features

Upload question paper and student answer sheet (PDF/Image)

Text extraction using OCR (Tesseract, PyPDF2)

AI-generated model answers using GPT4All

Answer comparison using Sentence Transformer

Automatic marks and grade calculation

SQLite database for storing results

Dashboard to view all student results

Download results as PDF

User-friendly web interface using Flask

🛠️ Technologies Used
Backend

Python

Flask

Frontend

HTML

CSS

AI / Machine Learning

SentenceTransformer (all-mpnet-base-v2)

GPT4All

OCR & File Handling

Pytesseract

PyPDF2

PIL (Pillow)

Database

SQLite

Other Libraries

FPDF

Regex

OS

🔄 System Workflow

User uploads question paper and answer sheet.

System extracts text from files using OCR.

Questions are separated and processed.

AI generates correct answers for each question.

Student answers are compared with model answers using semantic similarity.

Marks are calculated based on similarity score.

Grade is assigned.

Results are stored in SQLite database.

User can view results on dashboard and download as PDF.

🧩 Project Structure
AI-Exam-Evaluation-System/
│
├── app.py
├── exam.db
├── uploads/
├── templates/
│   ├── upload_questions.html
│   ├── result.html
│   └── dashboard.html
├── static/
│   └── style.css
├── README.md
└── requirements.txt

▶️ How to Run the Project
Step 1: Clone the Repository
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

📜 License

This project is for educational purposes only.
