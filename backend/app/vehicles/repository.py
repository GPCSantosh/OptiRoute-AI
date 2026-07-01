from sqlalchemy import select

from app.repositories.base import BaseRepository
from app.vehicles.models import Vehicle


class VehicleRepository(
    BaseRepository[Vehicle]
):

    def __init__(self, db):

        super().__init__(
            Vehicle,
            db,
        )

    async def get_by_registration(
        self,
        registration: str,
    ):

        result = await self.db.execute(
            select(Vehicle).where(
                Vehicle.registration_number == registration
            )
        )

        return result.scalar_one_or_none()

    async def available_vehicles(self):

        result = await self.db.execute(
            select(Vehicle).where(
                Vehicle.is_available.is_(True)
            )
        )

        return result.scalars().all()