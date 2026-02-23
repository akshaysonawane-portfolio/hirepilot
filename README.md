<p align="center">
  <h1>🚀 HirePilot — AI ATS & Job Application Assistant</h1>
</p>

<p align="center">
  A modern AI-powered assistant that helps job seekers optimize resumes, generate cover letters, request referrals, and track job applications — all in one clean dashboard.
</p>

---

## 📌 Overview

**HirePilot** is a full-stack AI application built using **Python**, **Streamlit**, and **OpenAI GPT models**.  
It helps job seekers speed up and streamline the job-application process by providing:

- ATS score & explanation  
- AI-generated cover letters  
- Professional referral request messages  
- Job tracking with status updates  
- Password-protected deployment  
- Modern, intuitive UI  

Designed as a **real portfolio project**, HirePilot demonstrates practical AI app development using the OpenAI API.

---

## ✨ Features

### 🧠 **AI Resume-to-JD Matching (ATS Score)**
- Upload your resume (PDF)
- Paste job description
- Embedding-based similarity scoring
- GPT-generated explanation

### ✉️ **AI Cover Letter Generator**
- Professional + friendly tone
- Personalized using resume + job description
- Crisp ~200-word format

### 🤝 **Referral Request Generator**
- Short, polite, and confident message
- Perfect for LinkedIn DMs or email

### 📅 **Job Application Tracker**
- Add: Company, Role, Date, Status  
- Update statuses easily  
- Stored locally using SQLite

### 🔒 **Password-Protected Deployment**
- Only you can access your hosted version  
- Prevents misuse and API credit drain

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI | OpenAI GPT-4.1, GPT-4.1-mini, text-embedding-3-small |
| Database | SQLite |
| Deployment | Streamlit Cloud |
| Secrets | `.streamlit/secrets.toml` |

---

## 🧩 Architecture
hirepilot/
│── app.py # Main Streamlit UI
│── backend/
│ ├── resume_parser.py # Extract text from PDFs
│ ├── embeddings.py # Embedding generator + similarity
│ ├── ats_analyzer.py # ATS score + GPT explanation
│ ├── cover_letter.py # Cover letter generator
│ ├── referral_generator.py # Referral message generator
│ ├── job_tracker.py # SQLite-based job tracking
│── data/
│ └── database.db # Local DB
│── .streamlit/
│ └── secrets.toml # Password + API key for cloud
│── requirements.txt # Dependencies
│── runtime.txt # Python version for Streamlit Cloud
└── README.md



---

## 💻 Local Installation

### 1️⃣ Clone the repo

```bash
git clone https://github.com/<your-username>/hirepilot.git
cd hirepilot
```

---

2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add your OpenAI key locally

Create .env:

OPENAI_API_KEY=your_key_here
5️⃣ Run the app
streamlit run app.py

App opens at:
👉 http://localhost:8501

🌐 Deploying to Streamlit Cloud
1️⃣ Push project to GitHub
2️⃣ Log in: https://share.streamlit.io
3️⃣ Create a new app

Repo: your GitHub repo

Branch: main

Main file: app.py

4️⃣ Add cloud secrets

Go to Settings → Secrets:

OPENAI_API_KEY="your_key"
password="yourpassword123"
5️⃣ Deploy 🎉

Your app goes live at:

https://<your-app-name>.streamlit.app

Password protected and safe.

🚀 Roadmap / Future Improvements

Skill gap analyzer (resume vs JD)

Resume rewriting with GPT

Multi-resume support

Export analysis as PDF

Job scraping from LinkedIn / Naukri

Dashboard analytics

Dark theme

🛡️ License

This project is licensed under the MIT License.

⭐ Support

If this project helped you, consider giving it a ⭐ star on GitHub!

<p align="center"><b>Built with ❤️ using Python & OpenAI</b></p> ```