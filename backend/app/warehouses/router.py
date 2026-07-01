from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import require_manager
from app.db.session import get_db
from app.users.models import User
from app.warehouses.repository import WarehouseRepository
from app.warehouses.schemas import (
    WarehouseCreate,
    WarehouseResponse,
)
from app.warehouses.service import WarehouseService

router = APIRouter(
    prefix="/warehouses",
    tags=["Warehouses"],
)


def get_service(
    db: AsyncSession = Depends(get_db),
):

    return WarehouseService(
        WarehouseRepository(db)
    )


@router.post(
    "/",
    response_model=WarehouseResponse,
)
async def create(
    payload: WarehouseCreate,
    service=Depends(get_service),
    _: User = Depends(
        require_manager()
    ),
):

    return await service.create(payload)


@router.get(
    "/",
    response_model=list[WarehouseResponse],
)
async def all(
    service=Depends(get_service),
):

    return await service.all()


@router.get(
    "/nearest",
    response_model=WarehouseResponse,
)
async def nearest(
    latitude: float = Query(...),
    longitude: float = Query(...),
    service=Depends(get_service),
):

    return await service.nearest_warehouse(
        latitude,
        longitude,
    )