from __future__ import annotations

from sqlalchemy.orm import Session

from app.users.models import User
from app.users.repository import UserRepository
from app.users.schemas import UserCreate
from app.users.schemas import UserUpdate
from app.core.security import get_password_hash


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def list_users(self):
        return self.repository.get_all()

    def get_user(self, user_id: int):
        return self.repository.get(user_id)

    def get_by_email(self, email: str):
        return self.repository.get_by_email(email)

    def create_user(self, payload: UserCreate):

        user = User(
            **payload.model_dump(
                exclude={"password"}
            )
        )

        user.hashed_password = get_password_hash(
            payload.password
        )

        return self.repository.create(user)

    def update_user(
        self,
        user_id: int,
        payload: UserUpdate,
    ):

        user = self.repository.get(user_id)

        if user is None:
            return None

        data = payload.model_dump(
            exclude_unset=True
        )

        if "password" in data:
            user.hashed_password = get_password_hash(
                data.pop("password")
            )

        for key, value in data.items():
            setattr(user, key, value)

        return self.repository.update(user)

    def delete_user(self, user_id: int):

        user = self.repository.get(user_id)

        if user is None:
            return False

        self.repository.delete(user)

        return True