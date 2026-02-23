# backend/ats_analyzer.py

from openai import OpenAI
import os
from dotenv import load_dotenv
from .embeddings import get_embedding, cosine_similarity

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GPT_MODEL = "gpt-4.1-mini"

def compute_ats_score(resume_text, jd_text):
    """
    Computes similarity score (0 to 100) between resume and job description.
    """
    try:
        resume_emb = get_embedding(resume_text)
        jd_emb = get_embedding(jd_text)

        similarity = cosine_similarity(resume_emb, jd_emb)
        score = round(similarity * 100, 2)

        return max(0, min(score, 100))  # Clamp between 0–100
    except Exception as e:
        return f"Error computing ATS score: {e}"


def explain_match(resume_text, jd_text):
    """
    GPT generates a simple explanation of the score.
    """
    prompt = f"""
    Resume Content:
    {resume_text}

    Job Description:
    {jd_text}

    Give a short explanation (3–5 lines) of how well the resume matches the job description.
    """

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]