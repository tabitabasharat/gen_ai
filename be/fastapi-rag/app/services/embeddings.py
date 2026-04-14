import ollama
import numpy as np
from app.config import EMBED_MODEL

def get_embedding(text: str):
    res = ollama.embeddings(
        model=EMBED_MODEL,
        prompt=text
    )
    return np.array(res["embedding"], dtype="float32")