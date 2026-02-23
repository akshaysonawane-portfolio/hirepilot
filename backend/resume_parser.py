# backend/resume_parser.py

import PyPDF2

def extract_text_from_pdf(pdf_file):
    """
    Extract raw text from a PDF resume.
    """
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"


def clean_resume_text(text: str) -> str:
    """
    Basic cleanup: remove extra spaces, newlines, etc.
    """
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text