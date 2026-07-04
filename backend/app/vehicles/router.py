from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.vehicles.schemas import (
    VehicleCreate,
    VehicleUpdate,
)
from app.vehicles.service import VehicleService

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)


@router.get("/")
async def list_vehicles(
    db: AsyncSession = Depends(get_db),
):
    return await VehicleService(db).list_vehicles()


@router.get("/{vehicle_id}")
async def get_vehicle(
    vehicle_id,
    db: AsyncSession = Depends(get_db),
):
    return await VehicleService(db).get_vehicle(
        vehicle_id
    )


@router.post("/")
async def create_vehicle(
    payload: VehicleCreate,
    db: AsyncSession = Depends(get_db),
):
    return await VehicleService(db).create_vehicle(
        payload
    )


@router.put("/{vehicle_id}")
async def update_vehicle(
    vehicle_id,
    payload: VehicleUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await VehicleService(db).update_vehicle(
        vehicle_id,
        payload,
    )


@router.delete("/{vehicle_id}")
async def delete_vehicle(
    vehicle_id,
    db: AsyncSession = Depends(get_db),
):
    success = await VehicleService(db).delete_vehicle(
        vehicle_id
    )

    return {
        "success": success
    }