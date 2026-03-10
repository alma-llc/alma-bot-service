from openai import AsyncOpenAI

from app.core.config import settings
from app.services import AIService


openai_client = AsyncOpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.openai_url
)


def get_ai_service() -> AIService:
    return AIService(openai_client)
