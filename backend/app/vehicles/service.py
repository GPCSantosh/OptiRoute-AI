from sqlalchemy.ext.asyncio import AsyncSession

from app.vehicles.models import Vehicle
from app.vehicles.repository import VehicleRepository
from app.vehicles.schemas import (
    VehicleCreate,
    VehicleUpdate,
)


class VehicleService:

    def __init__(self, db: AsyncSession):
        self.repository = VehicleRepository(db)

    async def list_vehicles(self):
        return await self.repository.get_all()

    async def get_vehicle(self, vehicle_id):
        return await self.repository.get(vehicle_id)

    async def create_vehicle(self, payload: VehicleCreate):

        vehicle = Vehicle(
            **payload.model_dump()
        )

        return await self.repository.create(vehicle)

    async def update_vehicle(
        self,
        vehicle_id,
        payload: VehicleUpdate,
    ):

        vehicle = await self.repository.get(vehicle_id)

        if vehicle is None:
            return None

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(vehicle, key, value)

        return await self.repository.update(vehicle)

        
    async def delete_vehicle(self, vehicle_id):

        vehicle = await self.repository.get(vehicle_id)

        if vehicle is None:
            return False

        await self.repository.delete(vehicle)

        return True
    