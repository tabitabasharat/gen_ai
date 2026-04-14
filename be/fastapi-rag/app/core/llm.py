import ollama
from app.config import LLM_MODEL

def generate_answer(context: str, question: str):
    prompt = f"""
You are a legal assistant.

RULES:
- Use ONLY the provided context
- If answer is not in context, say:
  "No relevant information found in documents"
- Do NOT guess

Context:
{context}

Question:
{question}
"""

    res = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return res["message"]["content"]