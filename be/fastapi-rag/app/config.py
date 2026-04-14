import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PDF_DIR = os.path.join(BASE_DIR, "rag_dataset")
VECTOR_DIR = os.path.join(BASE_DIR, "vectorstore")

FAISS_INDEX_PATH = os.path.join(VECTOR_DIR, "faiss_index.bin")
METADATA_PATH = os.path.join(VECTOR_DIR, "metadata.pkl")

EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "qwen"