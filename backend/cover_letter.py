# backend/cover_letter.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GPT_MODEL = "gpt-4.1"

def generate_cover_letter(resume_text, jd_text, applicant_name=""):
    """
    Generate cover letter using resume + job description.
    Tone: Professional + Friendly (Balanced)
    """

    prompt = f"""
    Write a concise cover letter (180–220 words).
    Tone: Professional + Friendly + Confident.
    Make it personalised and highlight the most relevant strengths.

    Applicant Name: {applicant_name if applicant_name else "The Candidate"}

    Resume Summary:
    {resume_text}

    Job Description:
    {jd_text}

    Structure:
    - Short intro
    - Why I'm a strong fit
    - Matching skills
    - Short, respectful closing

    Do NOT repeat the resume. Focus on alignment.
    """

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]