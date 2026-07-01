from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.base import BaseRepository
from app.users.models import User


class UserRepository(BaseRepository[User]):
    """
    Repository for User database operations.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(User, db)

    async def get_by_id(
        self,
        user_id: UUID,
    ) -> User | None:

        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )

        return result.scalar_one_or_none()

    async def get_by_email(
        self,
        email: str,
    ) -> User | None:

        result = await self.db.execute(
            select(User).where(User.email == email)
        )

        return result.scalar_one_or_none()

    async def get_by_username(
        self,
        username: str,
    ) -> User | None:

        result = await self.db.execute(
            select(User).where(User.username == username)
        )

        return result.scalar_one_or_none()

    async def create_user(
        self,
        user: User,
    ) -> User:

        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user

    async def update(
        self,
        user: User,
    ) -> User:

        await self.db.commit()

        await self.db.refresh(user)

        return user

    async def delete_user(
        self,
        user: User,
    ) -> None:

        await self.db.delete(user)

        await self.db.commit()