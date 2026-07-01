from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class RegisterRequest(BaseModel):
    first_name: str

    last_name: str

    username: str

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class RefreshRequest(BaseModel):
    refresh_token: str


class LogoutResponse(BaseModel):
    message: str


class TokenResponse(BaseModel):
    access_token: str

    refresh_token: str

    token_type: str = "Bearer"