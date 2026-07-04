from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.drivers.schemas import DriverCreate, DriverUpdate
from app.drivers.service import DriverService

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"],
)


@router.get("/")
async def list_drivers(
    db: AsyncSession = Depends(get_db),
):
    return await DriverService(db).list_drivers()


@router.get("/{driver_id}")
async def get_driver(
    driver_id,
    db: AsyncSession = Depends(get_db),
):
    return await DriverService(db).get_driver(driver_id)


@router.post("/")
async def create_driver(
    payload: DriverCreate,
    db: AsyncSession = Depends(get_db),
):
    return await DriverService(db).create_driver(payload)


@router.put("/{driver_id}")
async def update_driver(
    driver_id,
    payload: DriverUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await DriverService(db).update_driver(
        driver_id,
        payload,
    )


@router.delete("/{driver_id}")
async def delete_driver(
    driver_id,
    db: AsyncSession = Depends(get_db),
):
    success = await DriverService(db).delete_driver(
        driver_id
    )

    return {
        "success": success
    }