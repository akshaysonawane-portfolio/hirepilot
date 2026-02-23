# backend/referral_generator.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GPT_MODEL = "gpt-4.1-mini"

def generate_referral_message(candidate_name, job_role, company_name, resume_text):
    """
    Generates a short + polite referral request message.
    Ideal for LinkedIn DMs or email.
    """

    prompt = f"""
    Write a short referral request message.
    Tone: Polite + Direct + Respectful (balanced).
    Should sound confident but humble.

    Candidate: {candidate_name}
    Role: {job_role}
    Company: {company_name}

    Resume Summary:
    {resume_text}

    Requirements:
    - 3 to 5 lines max
    - No flattery or cringe
    - Clearly ask for referral
    - Mention relevant skills briefly
    - Keep it professional
    """

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]