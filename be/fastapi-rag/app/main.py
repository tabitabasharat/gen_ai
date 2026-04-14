from fastapi import FastAPI
from app.api import chat, ingest
from app.services.vectorstore import load
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RAG FastAPI Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(ingest.router)


@app.on_event("startup")
def startup():
    try:
        load()
        print("Vector DB loaded")
    except:
        print("No vector DB found. Run /ingest first.")