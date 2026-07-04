from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.roads.models import Road


class RoadRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    # ------------------------------------------
    # Get All
    # ------------------------------------------

    async def get_all(self):
        result = await self.db.execute(
            select(Road)
        )
        return result.scalars().all()

    # ------------------------------------------
    # Get By ID
    # ------------------------------------------

    async def get(
        self,
        road_id: UUID,
    ):
        result = await self.db.execute(
            select(Road).where(
                Road.id == road_id
            )
        )

        return result.scalar_one_or_none()

    async def get_by_id(
        self,
        road_id: UUID,
    ):
        return await self.get(road_id)

    # ------------------------------------------
    # Create
    # ------------------------------------------

    async def create(
        self,
        road: Road,
    ):
        self.db.add(road)

        await self.db.commit()

        await self.db.refresh(road)

        return road

    # ------------------------------------------
    # Update
    # ------------------------------------------

    async def update(
        self,
        road: Road,
    ):
        self.db.add(road)

        await self.db.commit()

        await self.db.refresh(road)

        return road

    # ------------------------------------------
    # Delete
    # ------------------------------------------

    async def delete(
        self,
        road: Road,
    ):
        await self.db.delete(road)

        await self.db.commit()