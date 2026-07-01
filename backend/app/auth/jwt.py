from datetime import datetime, timedelta, timezone
from uuid import uuid4

from jose import JWTError, jwt

from app.core.config import settings


class JWTManager:
    """
    JWT Token Manager
    """

    @staticmethod
    def create_access_token(
        user_id: str,
        email: str,
        username: str,
        role: str,
    ) -> str:

        now = datetime.now(timezone.utc)

        expire = now + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload = {
            "sub": user_id,
            "email": email,
            "username": username,
            "role": role,
            "type": "access",
            "iss": settings.APP_NAME,
            "iat": now,
            "exp": expire,
            "jti": str(uuid4()),
        }

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )

    @staticmethod
    def create_refresh_token(
        user_id: str,
    ) -> str:

        now = datetime.now(timezone.utc)

        expire = now + timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        )

        payload = {
            "sub": user_id,
            "type": "refresh",
            "iss": settings.APP_NAME,
            "iat": now,
            "exp": expire,
            "jti": str(uuid4()),
        }

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )

    @staticmethod
    def decode(
        token: str,
    ) -> dict:

        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
            issuer=settings.APP_NAME,
        )

    @staticmethod
    def verify_access_token(
        token: str,
    ) -> dict:

        payload = JWTManager.decode(token)

        if payload.get("type") != "access":
            raise JWTError("Invalid access token.")

        return payload

    @staticmethod
    def verify_refresh_token(
        token: str,
    ) -> dict:

        payload = JWTManager.decode(token)

        if payload.get("type") != "refresh":
            raise JWTError("Invalid refresh token.")

        return payload