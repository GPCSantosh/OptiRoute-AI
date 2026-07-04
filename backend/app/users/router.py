from fastapi import APIRouter
from fastapi import Depends

from app.auth.dependencies import get_current_user
from app.users.models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me", response_model=None)
async def get_current_user_profile(
    current_user: User = Depends(get_current_user),
):
    """
    Returns the currently authenticated user.
    """
    return current_user