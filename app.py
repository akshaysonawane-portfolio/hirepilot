# app.py

import streamlit as st
from backend.resume_parser import extract_text_from_pdf, clean_resume_text
from backend.ats_analyzer import compute_ats_score, explain_match
from backend.cover_letter import generate_cover_letter
from backend.referral_generator import generate_referral_message
from backend.job_tracker import init_db, add_job, get_all_jobs, update_status
import os

def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter password", type="password", on_change=password_entered, key="password")
        st.error("❌ Wrong password")
        return False
    return True


if not check_password():
    st.stop()
# Initialize DB
init_db()

# --- Page Config ---
st.set_page_config(
    page_title="HirePilot – AI ATS & Job Tracker",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 HirePilot – AI ATS & Job Tracker")
st.write("AI-powered resume matching, cover letters, referral messages & job tracking.")

# Sidebar Menu
menu = st.sidebar.radio(
    "Navigation",
    ["ATS Score", "Cover Letter", "Referral Message", "Job Tracker"]
)

# ============================
#     ATS SCORE SECTION
# ============================
if menu == "ATS Score":
    st.header("📊 ATS Resume Score")

    resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    jd_text = st.text_area("Paste Job Description", height=200)

    if resume_file and jd_text:
        if st.button("Calculate ATS Score"):
            with st.spinner("Processing resume..."):
                resume_raw = extract_text_from_pdf(resume_file)
                resume_text = clean_resume_text(resume_raw)

                score = compute_ats_score(resume_text, jd_text)
                explanation = explain_match(resume_text, jd_text)

            st.subheader(f"⭐ ATS Match Score: **{score}/100**")
            st.write(explanation)


# ============================
#     COVER LETTER SECTION
# ============================
if menu == "Cover Letter":
    st.header("✉️ AI Cover Letter Generator")

    resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    jd_text = st.text_area("Paste Job Description", height=200)
    applicant_name = st.text_input("Your Name (optional)")

    if resume_file and jd_text:
        if st.button("Generate Cover Letter"):
            with st.spinner("Creating your cover letter..."):
                resume_raw = extract_text_from_pdf(resume_file)
                resume_text = clean_resume_text(resume_raw)

                cover_letter = generate_cover_letter(resume_text, jd_text, applicant_name)

            st.subheader("📄 Your Cover Letter")
            st.write(cover_letter)


# ============================
#     REFERRAL MESSAGE
# ============================
if menu == "Referral Message":
    st.header("🤝 Referral Request Generator")

    candidate_name = st.text_input("Your Name", placeholder="Akshay")
    job_role = st.text_input("Job Role", placeholder="Software Engineer")
    company_name = st.text_input("Company Name", placeholder="Deloitte")
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if resume_file and candidate_name and job_role and company_name:
        if st.button("Generate Referral Message"):
            with st.spinner("Generating message..."):
                resume_raw = extract_text_from_pdf(resume_file)
                resume_text = clean_resume_text(resume_raw)

                message = generate_referral_message(
                    candidate_name, job_role, company_name, resume_text
                )

            st.subheader("📩 Referral Message")
            st.write(message)


# ============================
#       JOB TRACKER
# ============================
if menu == "Job Tracker":
    st.header("📅 Job Application Tracker")

    st.subheader("Add New Job")
    company = st.text_input("Company")
    role = st.text_input("Role")
    status = st.selectbox("Status", ["Applied", "Interviewing", "Rejected", "Offer"])

    if st.button("Add Job"):
        add_job(company, role, status)
        st.success("Job added successfully!")

    st.subheader("📌 Your Applications")
    jobs = get_all_jobs()

    if jobs:
        for job in jobs:
            job_id, comp, role, date, stat = job
            st.write(f"**{comp}** – {role} | {date} | Status: {stat}")

            new_stat = st.selectbox(
                f"Update Status (Job ID: {job_id})",
                ["Applied", "Interviewing", "Rejected", "Offer"],
                index=["Applied", "Interviewing", "Rejected", "Offer"].index(stat),
                key=f"status_{job_id}"
            )

            if st.button(f"Save {job_id}"):
                update_status(job_id, new_stat)
                st.success("Updated!")
    else:
        st.info("No jobs added yet.")

