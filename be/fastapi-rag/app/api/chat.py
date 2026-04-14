from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.core.rag_pipeline import ask

router = APIRouter()

@router.post("/chat")
async def chat(req: ChatRequest):
    # If ask() is a regular function, this is fine. 
    # If ask() calls an OpenAI/LLM API, it should ideally be async.
    return ask(req.question)
