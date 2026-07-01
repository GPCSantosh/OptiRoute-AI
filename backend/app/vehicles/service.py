from app.exceptions.base import ConflictException
from app.vehicles.models import Vehicle
from app.vehicles.repository import VehicleRepository
from app.vehicles.schemas import VehicleCreate


class VehicleService:

    def __init__(
        self,
        repository: VehicleRepository,
    ):

        self.repository = repository

    async def create_vehicle(
        self,
        payload: VehicleCreate,
    ):

        existing = await self.repository.get_by_registration(
            payload.registration_number
        )

        if existing:

            raise ConflictException(
                "Vehicle already exists."
            )

        vehicle = Vehicle(
            **payload.model_dump()
        )

        return await self.repository.create(
            vehicle
        )

    async def get_all(self):

        return await self.repository.get_all()

    async def available(self):

        return await self.repository.available_vehicles()