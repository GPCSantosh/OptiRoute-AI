from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.users.models import UserRole


class UserCreate(BaseModel):

    first_name: str = Field(
        min_length=2,
        max_length=100,
    )

    last_name: str = Field(
        min_length=2,
        max_length=100,
    )

    username: str = Field(
        min_length=4,
        max_length=50,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class UserLogin(BaseModel):

    email: EmailStr

    password: str


class UserUpdate(BaseModel):

    first_name: str | None = None

    last_name: str | None = None


class UserResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    first_name: str

    last_name: str

    username: str

    email: EmailStr

    role: UserRole

    is_active: bool

    is_verified: bool

    created_at: datetime


class Token(BaseModel):

    access_token: str

    refresh_token: str

    token_type: str = "bearer"


class TokenPayload(BaseModel):

    sub: str

    type: str

    exp: int

class RefreshTokenRequest(BaseModel):
    refresh_token: str