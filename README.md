📚 **RAG Project** (Notebook → FastAPI → Frontend Integration)

🚀** Overview**

This project demonstrates a complete Retrieval-Augmented Generation (RAG) system built in multiple stages:

1.First we developed and tested the system in a Jupyter Notebook

2.Then we converted the logic into a FastAPI backend

3.Finally, we integrated the backend with a frontend application

The goal is to understand how a RAG pipeline moves from research → production.


🧠 **Project Workflow**

1️⃣ Notebook Phase (Research & Experimentation)

In the first step, we built the entire RAG pipeline inside a Jupyter Notebook.

What we did in Notebook:
Loaded PDF documents
Converted text into chunks
Generated embeddings using a model
Stored embeddings in FAISS vector database
Performed similarity search
Generated answers using an LLM
Purpose:

This phase was used for:

Testing ideas quickly
Debugging logic
Understanding RAG flow step-by-step
2️⃣ Backend Phase (FastAPI Conversion)

After validating the notebook, we converted everything into a production-ready backend using FastAPI.

What we implemented in FastAPI:
📌 API Endpoints
/ingest → Loads documents and builds vector database
/chat → Accepts user query and returns AI response
📌 Core Components
PDF loader service
Text chunking module
Embedding generator
FAISS vector store
RAG pipeline logic
LLM response generation
Backend Architecture:
User Query → Embedding → FAISS Search → Context Retrieval → LLM → Answer
Purpose:
Convert research code into scalable API
Enable real-time interaction with RAG system
3️⃣ Frontend Integration Phase

In the final step, we connected the backend with a frontend application.

What we did:
Built UI for user query input
Sent API requests to FastAPI backend
Displayed AI-generated responses
Handled loading states and errors
Flow:
Frontend UI → /chat API → FastAPI → RAG Pipeline → Response → UI Display
🔗 Full System Architecture
<img width="338" height="420" alt="image" src="https://github.com/user-attachments/assets/51cdc075-7bbd-4179-886b-8f6b89a664e2" />


🧩 Tech Stack
Python 🐍
FastAPI ⚡
FAISS (Vector Database)
NumPy
LLM (Ollama / OpenAI / Qwen)
HTML / JavaScript (Frontend)
📌 Key Learnings
Notebook Phase:
How embeddings work
How vector search retrieves similar text
How LLM uses context to generate answers
Backend Phase:
How to structure APIs using FastAPI
How to convert notebook code into modular services
How to manage vector databases in production
Frontend Phase:
How frontend communicates with backend APIs
How to display AI responses in real-time
