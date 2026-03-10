from openai import AsyncOpenAI

from core.config import settings


class AIService:
    def __init__(self, client: AsyncOpenAI):
        self.client = client

    async def generate_reply(self, message: str, prompt: str) -> str:
        response = await self.client.responses.create(
            model=settings.openai_model,
            instructions=prompt,
            input=message,
        )
        return response.output_text
