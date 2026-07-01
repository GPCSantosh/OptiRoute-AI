from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.jwt import JWTManager
from app.auth.service import AuthService
from app.db.session import get_db
from app.exceptions.base import (
    ForbiddenException,
    UnauthorizedException,
)
from app.users.models import User, UserRole
from app.users.repository import UserRepository

security = HTTPBearer(
    auto_error=True
)


def get_auth_service(
    db: AsyncSession = Depends(get_db),
) -> AuthService:

    return AuthService(
        UserRepository(db)
    )


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    service: AuthService = Depends(
        get_auth_service
    ),
) -> User:

    token = credentials.credentials

    try:

        payload = JWTManager.verify_access_token(
            token
        )

    except JWTError:

        raise UnauthorizedException(
            "Invalid or expired token."
        )

    user = await service.get_current_user(
        UUID(payload["sub"])
    )

    if not user.is_active:

        raise UnauthorizedException(
            "User is inactive."
        )

    return user

def require_admin():

    async def dependency(
        current_user: User = Depends(
            get_current_user
        ),
    ):

        if current_user.role != UserRole.ADMIN:

            raise ForbiddenException(
                "Admin privileges required."
            )

        return current_user

    return dependency


def require_manager():

    async def dependency(
        current_user: User = Depends(
            get_current_user
        ),
    ):

        if current_user.role not in (
            UserRole.ADMIN,
            UserRole.MANAGER,
        ):

            raise ForbiddenException(
                "Manager privileges required."
            )

        return current_user

    return dependency


def require_dispatcher():

    async def dependency(
        current_user: User = Depends(
            get_current_user
        ),
    ):

        if current_user.role not in (
            UserRole.ADMIN,
            UserRole.MANAGER,
            UserRole.DISPATCHER,
        ):

            raise ForbiddenException(
                "Dispatcher privileges required."
            )

        return current_user

    return dependency