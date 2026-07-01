from sqlalchemy import select

from app.repositories.base import BaseRepository
from app.warehouses.models import Warehouse


class WarehouseRepository(
    BaseRepository[Warehouse]
):

    def __init__(self, db):

        super().__init__(
            Warehouse,
            db,
        )

    async def get_by_code(
        self,
        code: str,
    ):

        result = await self.db.execute(
            select(Warehouse).where(
                Warehouse.warehouse_code == code
            )
        )

        return result.scalar_one_or_none()

    async def active_warehouses(self):

        result = await self.db.execute(
            select(Warehouse).where(
                Warehouse.is_active.is_(True)
            )
        )

        return result.scalars().all()