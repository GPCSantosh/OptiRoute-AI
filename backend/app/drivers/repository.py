from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.drivers.models import Driver


class DriverRepository:

    def __init__(self, db: AsyncSession):
        self.db = db
    async def get(
        self,
        driver_id: UUID,
    ):
        result = await self.db.execute(
            select(Driver).where(
                Driver.id == driver_id
            )
        )
        return result.scalar_one_or_none()
    
    async def get_all(self):
        result = await self.db.execute(select(Driver))
        return result.scalars().all()

    async def get_by_id(self, driver_id: UUID):
        result = await self.db.execute(
            select(Driver).where(Driver.id == driver_id)
        )
        return result.scalar_one_or_none()

    async def create(self, driver: Driver):
        self.db.add(driver)
        await self.db.commit()
        await self.db.refresh(driver)
        return driver

    async def update(self, driver: Driver):
        self.db.add(driver)
        await self.db.commit()
        await self.db.refresh(driver)
        return driver

    async def delete(self, driver: Driver):
        await self.db.delete(driver)
        await self.db.commit()