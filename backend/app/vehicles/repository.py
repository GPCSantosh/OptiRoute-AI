from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.vehicles.models import Vehicle


class VehicleRepository:

    def __init__(self, db: AsyncSession):
        self.db = db
    async def get(self, vehicle_id: UUID):
        result = await self.db.execute(
            select(Vehicle).where(
                Vehicle.id == vehicle_id
            )
        )
        return result.scalar_one_or_none()
    
    async def get_all(self):
        result = await self.db.execute(select(Vehicle))
        return result.scalars().all()

    async def get_by_id(self, vehicle_id: UUID):
        result = await self.db.execute(
            select(Vehicle).where(
                Vehicle.id == vehicle_id
            )
        )
        return result.scalar_one_or_none()

    async def create(self, vehicle: Vehicle):
        self.db.add(vehicle)
        await self.db.commit()
        await self.db.refresh(vehicle)
        return vehicle

    async def update(self, vehicle: Vehicle):
        self.db.add(vehicle)
        await self.db.commit()
        await self.db.refresh(vehicle)
        return vehicle

    async def delete(self, vehicle: Vehicle):
        await self.db.delete(vehicle)
        await self.db.commit()