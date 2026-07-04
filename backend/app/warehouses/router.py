from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.warehouses.schemas import (
    WarehouseCreate,
    WarehouseUpdate,
)
from app.warehouses.service import WarehouseService

router = APIRouter(
    prefix="/warehouses",
    tags=["Warehouses"],
)


@router.get("/")
async def list_warehouses(
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService(db).list_warehouses()


@router.get("/{warehouse_id}")
async def get_warehouse(
    warehouse_id,
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService(db).get_warehouse(
        warehouse_id
    )


@router.post("/")
async def create_warehouse(
    payload: WarehouseCreate,
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService(db).create_warehouse(
        payload
    )


@router.put("/{warehouse_id}")
async def update_warehouse(
    warehouse_id,
    payload: WarehouseUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await WarehouseService(db).update_warehouse(
        warehouse_id,
        payload,
    )


@router.delete("/{warehouse_id}")
async def delete_warehouse(
    warehouse_id,
    db: AsyncSession = Depends(get_db),
):
    success = await WarehouseService(db).delete_warehouse(
        warehouse_id
    )

    return {"success": success}