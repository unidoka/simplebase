import redis.asyncio as aioredis
from .config import settings

valkey_client = None

async def get_valkey():
    global valkey_client
    if valkey_client is None:
        valkey_client = aioredis.from_url(settings.VALKEY_URL, decode_responses=True)
    return valkey_client
