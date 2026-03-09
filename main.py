from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.v1 import chat_router
from db.redis.client import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.ping()
    try:
        yield
    finally:
        await redis_client.aclose()

app = FastAPI(title="AI Chatbot API", lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(chat_router)
