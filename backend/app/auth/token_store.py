from redis.asyncio import Redis

from app.core.config import settings


class TokenStore:

    def __init__(self):

        self.redis = Redis.from_url(
            settings.REDIS_URL,
            decode_responses=True,
        )

    async def save_refresh_token(
        self,
        user_id: str,
        token: str,
        ttl: int,
    ):

        await self.redis.setex(
            f"refresh:{user_id}",
            ttl,
            token,
        )

    async def get_refresh_token(
        self,
        user_id: str,
    ):

        return await self.redis.get(
            f"refresh:{user_id}"
        )

    async def revoke_refresh_token(
        self,
        user_id: str,
    ):

        await self.redis.delete(
            f"refresh:{user_id}"
        )