from fastapi import APIRouter
from fastapi import Depends

from app.auth.dependencies import (
    get_current_user,
)
from app.users.models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
async def me(
    current_user: User = Depends(
        get_current_user
    ),
):
    return current_user

from app.users.router import router as users_router

app.include_router(
    users_router,
    prefix=settings.API_V1_PREFIX,
)