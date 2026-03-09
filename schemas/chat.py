from pydantic import BaseModel
from typing import Literal, Optional


class ChatMessage(BaseModel):
    role: Literal["user", "ai"]
    user_id: Optional[int] = None
    content: str


class ChatRequest(BaseModel):
    user_id: int
    message: str


class ChatResponse(BaseModel):
    message: str
