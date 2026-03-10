from fastapi import APIRouter, Depends
from redis.asyncio import Redis

from integrations.openai import get_ai_service
from integrations.redis import get_redis
from schemas.chat import ChatRequest
from services import AIService
from processors.prompt_builder import PromptBuilder

router = APIRouter(prefix="/chat", tags=["chat"])
prompt_builder = PromptBuilder()


@router.post("/")
async def chat_message(
    request: ChatRequest,
    redis: Redis = Depends(get_redis),
    ai_service: AIService = Depends(get_ai_service)
):
    ai_response = await ai_service.generate_reply(
        request.message,
        prompt_builder.build_chat_prompt()
    )
    return {"message": ai_response}
