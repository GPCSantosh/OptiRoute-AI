from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.models import User


class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    # ---------------------------------------------------
    # Get all users
    # ---------------------------------------------------

    async def get_all(self):
        result = await self.db.execute(
            select(User)
        )
        return result.scalars().all()

    # ---------------------------------------------------
    # Get by ID
    # ---------------------------------------------------

    async def get_by_id(
        self,
        user_id: UUID,
    ):
        result = await self.db.execute(
            select(User).where(
                User.id == user_id
            )
        )

        return result.scalar_one_or_none()

    # ---------------------------------------------------
    # Get by Email
    # ---------------------------------------------------

    async def get_by_email(
        self,
        email: str,
    ):
        result = await self.db.execute(
            select(User).where(
                User.email == email
            )
        )

        return result.scalar_one_or_none()

    # ---------------------------------------------------
    # Get by Username
    # ---------------------------------------------------

    async def get_by_username(
        self,
        username: str,
    ):
        result = await self.db.execute(
            select(User).where(
                User.username == username
            )
        )

        return result.scalar_one_or_none()

    # ---------------------------------------------------
    # Create User
    # ---------------------------------------------------

    async def create_user(
        self,
        user: User,
    ):
        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user

    # ---------------------------------------------------
    # Update User
    # ---------------------------------------------------

    async def update(
        self,
        user: User,
    ):
        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user

    # ---------------------------------------------------
    # Delete User
    # ---------------------------------------------------

    async def delete(
        self,
        user: User,
    ):
        await self.db.delete(user)

        await self.db.commit()