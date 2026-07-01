from app.drivers.models import Driver
from app.drivers.repository import DriverRepository
from app.drivers.schemas import DriverCreate
from app.exceptions.base import ConflictException


class DriverService:

    def __init__(
        self,
        repository: DriverRepository,
    ):

        self.repository = repository

    async def create_driver(
        self,
        payload: DriverCreate,
    ):

        existing = await self.repository.get_by_employee_id(
            payload.employee_id
        )

        if existing:

            raise ConflictException(
                "Employee ID already exists."
            )

        driver = Driver(
            **payload.model_dump()
        )

        return await self.repository.create(
            driver
        )

    async def get_all_drivers(self):

        return await self.repository.get_all()

    async def available_drivers(self):

        return await self.repository.get_available_drivers()