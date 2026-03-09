from fastapi import APIRouter, Depends
from redis.asyncio import Redis

from api.deps import get_redis
from schemas.chat import ChatRequest
from services.chat_service import add_chat_message, get_chat_history

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/")
async def chat_message(request: ChatRequest, redis: Redis = Depends(get_redis)):
    await add_chat_message(redis, request.user_id, request.message)
    return {"message": "Added message to chat history!"}


@router.get("/history")
async def chat_history(user_id: int, redis: Redis = Depends(get_redis)):
    history = await get_chat_history(redis, user_id)
    return {"history": history}
