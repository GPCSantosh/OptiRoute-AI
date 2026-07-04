from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.warehouses.models import Warehouse

class WarehouseRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, entity_id):
        result = await self.db.execute(
            select(Warehouse).where(Warehouse.id == entity_id)
        )
        return result.scalar_one_or_none()

    async def update(self, entity):

        try:
            await self.db.commit()
            await self.db.refresh(entity)
            return entity

        except Exception:
            await self.db.rollback()
            raise
    
    async def delete(self, warehouse):

        await self.db.delete(warehouse)

        await self.db.commit()

    async def get_all(self):

        result = await self.db.execute(
            select(Warehouse)
        )

        return result.scalars().all()

    async def get_by_id(self, warehouse_id):

        result = await self.db.execute(
            select(Warehouse).where(
                Warehouse.id == warehouse_id
            )
        )

        return result.scalar_one_or_none()


    async def create(self, warehouse):

        try:
            self.db.add(warehouse)

            await self.db.commit()

            await self.db.refresh(warehouse)

            return warehouse

        except IntegrityError:
            await self.db.rollback()
            raise