from sqlalchemy.ext.asyncio import AsyncSession

from app.drivers.models import Driver
from app.drivers.repository import DriverRepository
from app.drivers.schemas import DriverCreate, DriverUpdate


class DriverService:

    def __init__(self, db: AsyncSession):
        self.repository = DriverRepository(db)

    async def list_drivers(self):
        return await self.repository.get_all()

    async def get_driver(self, driver_id):
        return await self.repository.get(driver_id)

    async def create_driver(
        self,
        payload: DriverCreate,
    ):
        driver = Driver(
            **payload.model_dump()
        )

        return await self.repository.create(driver)

    async def update_driver(
        self,
        driver_id,
        payload: DriverUpdate,
    ):
        driver = await self.repository.get_by_id(driver_id)

        if driver is None:
            return None

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(driver, key, value)

        return await self.repository.update(driver)

    async def delete_driver(
        self,
        driver_id,
    ):
        driver = await self.repository.get_by_id(driver_id)

        if driver is None:
            return False

        await self.repository.delete(driver)

        return True