from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import (
    get_auth_service,
    get_current_user,
)
from app.auth.service import AuthService
from app.db.session import get_db
from app.users.models import User
from app.users.schemas import (
    RefreshTokenRequest,
    Token,
    UserCreate,
    UserLogin,
    UserResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    payload: UserCreate,
    service: AuthService = Depends(get_auth_service),
):

    return await service.register(payload)


@router.post(
    "/login",
    response_model=Token,
)
async def login(
    payload: UserLogin,
    service: AuthService = Depends(get_auth_service),
):

    return await service.login(payload)


@router.get(
    "/me",
    response_model=UserResponse,
)
async def me(
    current_user: User = Depends(
        get_current_user
    ),
):

    return current_user


@router.post("/logout")
async def logout(
    current_user: User = Depends(
        get_current_user
    ),
    service: AuthService = Depends(
        get_auth_service
    ),
):

    await service.logout(
        str(current_user.id)
    )

    return {
        "message": "Logged out successfully."
    }


@router.post(
    "/refresh",
    response_model=Token,
)
async def refresh(
    payload: RefreshTokenRequest,
    service: AuthService = Depends(
        get_auth_service
    ),
):

    return await service.refresh_access_token(
        payload.refresh_token
    )