from app.users.models import User, UserRole  # adjust the import if your enum is elsewhere
from uuid import UUID
from datetime import datetime

from app.auth.jwt import JWTManager
from app.auth.password import PasswordManager
from app.auth.token_store import TokenStore
from app.core.config import settings
from app.exceptions.base import (
    ConflictException,
    NotFoundException,
    UnauthorizedException,
)
from app.users.models import User
from app.users.repository import UserRepository
from app.users.schemas import (
    Token,
    UserCreate,
    UserLogin,
)
from app.utils.time import utc_now


class AuthService:
    """
    Authentication Business Logic
    """

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository
        self.token_store = TokenStore()

    # --------------------------------------------------
    # Register
    # --------------------------------------------------

    async def register(
        self,
        payload: UserCreate,
    ) -> User:

        existing_email = await self.repository.get_by_email(
            payload.email
        )

        if existing_email:
            raise ConflictException(
                "Email already registered."
            )

        existing_username = await self.repository.get_by_username(
            payload.username
        )

        if existing_username:
            raise ConflictException(
                "Username already exists."
            )


        user = User(
            first_name=payload.first_name,
            last_name=payload.last_name,
            username=payload.username,
            email=payload.email,
            password_hash=PasswordManager.hash(payload.password),
            role=UserRole.ADMIN,
            is_active=True,
            is_verified=True,
        )

        return await self.repository.create_user(user)

    # --------------------------------------------------
    # Login
    # --------------------------------------------------

    async def login(
        self,
        payload: UserLogin,
    ) -> Token:
        print("LOGIN EMAIL:", payload.email)

        user = await self.repository.get_by_email(
            payload.email
        )

        print("USER:", user)

        if user:
            print("HASH:", user.password_hash)

        user = await self.repository.get_by_email(
            payload.email
        )

        if user is None:
            raise UnauthorizedException(
                "Invalid email or password."
            )

        if not PasswordManager.verify(
            payload.password,
            user.password_hash,
        ):
            raise UnauthorizedException(
                "Invalid email or password."
            )


        user.last_login = utc_now()

        await self.repository.update(user)

        role = (
            user.role.value
            if user.role is not None
            else "ADMIN"
        )

        access_token = JWTManager.create_access_token(
            str(user.id),
            user.email,
            user.username,
            role,
        )

        refresh_token = JWTManager.create_refresh_token(
            str(user.id)
        )

        await self.token_store.save_refresh_token(
            str(user.id),
            refresh_token,
            settings.REFRESH_TOKEN_EXPIRE_DAYS * 86400,
        )

        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    # --------------------------------------------------
    # Current User
    # --------------------------------------------------

    async def get_current_user(
        self,
        user_id: UUID,
    ) -> User:

        user = await self.repository.get_by_id(
            user_id
        )

        if user is None:
            raise NotFoundException(
                "User not found."
            )

        return user

    # --------------------------------------------------
    # Change Password
    # --------------------------------------------------

    async def change_password(
        self,
        user_id: UUID,
        old_password: str,
        new_password: str,
    ) -> None:

        user = await self.repository.get_by_id(
            user_id
        )

        if user is None:
            raise NotFoundException(
                "User not found."
            )

        if not PasswordManager.verify(
            old_password,
            user.password_hash,
        ):
            raise UnauthorizedException(
                "Old password is incorrect."
            )

        user.password_hash = PasswordManager.hash(
            new_password
        )

        await self.repository.update(user)

    # --------------------------------------------------
    # Refresh Access Token
    # --------------------------------------------------

    async def refresh_access_token(
        self,
        refresh_token: str,
    ) -> Token:

        payload = JWTManager.verify_refresh_token(
            refresh_token
        )

        user = await self.get_current_user(
            UUID(payload["sub"])
        )

        stored_token = await self.token_store.get_refresh_token(
            str(user.id)
        )

        if stored_token != refresh_token:
            raise UnauthorizedException(
                "Refresh token has been revoked."
            )

        access_token = JWTManager.create_access_token(
            str(user.id),
            user.email,
            user.username,
            user.role.value,
        )

        new_refresh_token = JWTManager.create_refresh_token(
            str(user.id)
        )

        await self.token_store.save_refresh_token(
            str(user.id),
            new_refresh_token,
            settings.REFRESH_TOKEN_EXPIRE_DAYS * 86400,
        )

        return Token(
            access_token=access_token,
            refresh_token=new_refresh_token,
        )

    # --------------------------------------------------
    # Logout
    # --------------------------------------------------

    async def logout(
        self,
        user_id: str,
    ) -> None:

        await self.token_store.revoke_refresh_token(
            user_id
        )