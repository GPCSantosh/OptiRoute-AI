from sqlalchemy import select

from app.drivers.models import Driver
from app.repositories.base import BaseRepository


class DriverRepository(
    BaseRepository[Driver]
):

    def __init__(self, db):

        super().__init__(
            Driver,
            db,
        )

    async def get_by_employee_id(
        self,
        employee_id: str,
    ):

        result = await self.db.execute(
            select(Driver).where(
                Driver.employee_id == employee_id
            )
        )

        return result.scalar_one_or_none()

    async def get_available_drivers(self):

        result = await self.db.execute(
            select(Driver).where(
                Driver.is_available == True
            )
        )

        return result.scalars().all()