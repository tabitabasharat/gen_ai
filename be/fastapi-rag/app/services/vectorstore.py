import faiss
import pickle

index = None
chunks = []


def save(index_obj, chunks_list):
    faiss.write_index(index_obj, "vectorstore/faiss_index.bin")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks_list, f)


def load():
    global index, chunks   # 🔥 VERY IMPORTANT

    index = faiss.read_index("vectorstore/faiss_index.bin")

    with open("vectorstore/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks
def search(query_vec, k=4):
    global index

    if index is None:
        load()

    scores, idx = index.search(query_vec, k)
    return scores[0], idx[0]