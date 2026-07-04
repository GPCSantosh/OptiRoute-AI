from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.warehouses.models import Warehouse
from app.warehouses.repository import WarehouseRepository
from app.warehouses.schemas import (
    WarehouseCreate,
    WarehouseUpdate,
)


class WarehouseService:

    def __init__(self, db: AsyncSession):
        self.repository = WarehouseRepository(db)

    async def list_warehouses(self):
        return await self.repository.get_all()

    async def get_warehouse(self, warehouse_id):
        return await self.repository.get(warehouse_id)

    # from fastapi import HTTPException

    async def create_warehouse(self, warehouse: WarehouseCreate):

        db_warehouse = Warehouse(
            warehouse_code=warehouse.warehouse_code,
            warehouse_name=warehouse.warehouse_name,
            address=warehouse.address,
            city=warehouse.city,
            state=warehouse.state,
            latitude=warehouse.latitude,
            longitude=warehouse.longitude,
            total_capacity=warehouse.total_capacity,
            available_capacity=warehouse.total_capacity,
            is_active=True,
        )

        try:
            return await self.repository.create(db_warehouse)

        except IntegrityError:
            raise HTTPException(
                status_code=409,
                detail="Warehouse code already exists."
            )

    async def update_warehouse(
        self,
        warehouse_id,
        payload: WarehouseUpdate,
    ):

        warehouse = await self.repository.get(warehouse_id)

        if warehouse is None:
            raise HTTPException(
                status_code=404,
                detail="Warehouse not found"
            )

        data = payload.model_dump(exclude_none=True)

        for key, value in data.items():
            setattr(warehouse, key, value)

        return await self.repository.update(warehouse)

    async def delete_warehouse(
        self,
        warehouse_id,
    ):

        warehouse = await self.repository.get(
            warehouse_id
        )

        if warehouse is None:
            return False

        await self.repository.delete(
            warehouse
        )

        return True