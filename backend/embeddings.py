# backend/embeddings.py

from openai import OpenAI
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMBEDDING_MODEL = "text-embedding-3-small"

def get_embedding(text: str):
    """
    Returns embedding vector using OpenAI's embedding model.
    """
    text = text.replace("\n", " ")

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return np.array(response.data[0].embedding)


def cosine_similarity(a, b):
    """
    Compute cosine similarity between two vectors.
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))