from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.core.rag_pipeline import ask

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    return ask(req.question)