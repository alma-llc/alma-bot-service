from redis.asyncio import Redis


async def get_chat_history(redis: Redis, user_id: int):
    return await redis.lrange(f"chat_history:{user_id}:messages", 0, -1)


async def add_chat_message(redis: Redis, user_id: int, message: str):
    await redis.rpush(f"chat_history:{user_id}:messages", message)
