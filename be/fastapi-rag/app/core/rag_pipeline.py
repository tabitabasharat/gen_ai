import numpy as np
from app.services.embeddings import get_embedding
from app.services.vectorstore import index, chunks, search
from app.core.llm import generate_answer


def retrieve(question):
    query_vec = np.array(get_embedding(question)).astype("float32").reshape(1, -1)

    scores, I = index.search(query_vec, k=3)

    valid_chunks = []
    valid_scores = []

    for i, score in zip(I[0], scores[0]):
        if i < len(chunks):
            valid_chunks.append(chunks[i])
            valid_scores.append(float(score))

    return valid_chunks, valid_scores


def ask(question: str):
    contexts, scores = retrieve(question)

    if not scores:
        return {
            "answer": "No relevant information found.",
            "scores": []
        }

    best_score = max(scores)

    if best_score < 0.70:
        return {
            "answer": "No relevant information found in documents.",
            "scores": scores
        }

    context_text = "\n\n".join(contexts)

    answer = generate_answer(context_text, question)

    return {
        "answer": answer,
        "scores": scores
    }