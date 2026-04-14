import faiss
import pickle
import os

# Define paths
INDEX_PATH = "vectorstore/faiss_index.bin"
CHUNKS_PATH = "vectorstore/chunks.pkl"

# Initialize as None/Empty
index = None
chunks = []

def load():
    global index, chunks
    if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):
        try:
            index = faiss.read_index(INDEX_PATH)
            with open(CHUNKS_PATH, "rb") as f:
                chunks = pickle.load(f)
            print("✅ Vectorstore loaded successfully.")
        except Exception as e:
            print(f"❌ Error loading vectorstore: {e}")
    else:
        print("⚠️ Vectorstore files not found. Please run the ingestion script first.")

def save(index_obj, chunks_list):
    global index, chunks
    os.makedirs("vectorstore", exist_ok=True)
    faiss.write_index(index_obj, INDEX_PATH)
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks_list, f)
    # Update global state after saving
    index = index_obj
    chunks = chunks_list

def search(query_vec, k=4):
    global index
    if index is None:
        load()
    
    if index is None:
        raise ValueError("Index is still None. Ensure 'faiss_index.bin' exists.")

    scores, idx = index.search(query_vec, k)
    return scores, idx

# 🔥 Auto-load when the module is first imported
load()
