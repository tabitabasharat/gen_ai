from fastapi import APIRouter
import numpy as np
import faiss

from app.config import PDF_DIR
from app.services.loader import load_pdfs
from app.services.chunking import chunk_text
from app.services.embeddings import get_embedding
from app.services.vectorstore import save, load   # ✅ ADD load

router = APIRouter()


@router.post("/ingest")
def ingest():
    docs = load_pdfs(PDF_DIR)

    chunks = []
    for d in docs:
        chunks.extend(chunk_text(d))

    embeddings = np.array([get_embedding(c) for c in chunks])

    # normalize for cosine similarity
    faiss.normalize_L2(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    save(index, chunks)

    load()  # ✅ IMPORTANT: reload into memory

    return {
        "message": "Ingestion complete",
        "chunks": len(chunks)
    }