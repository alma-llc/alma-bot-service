from db.redis.client import redis_client


async def get_redis():
    return redis_client
