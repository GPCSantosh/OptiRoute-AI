from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import require_manager
from app.db.session import get_db
from app.users.models import User
from app.vehicles.repository import VehicleRepository
from app.vehicles.schemas import (
    VehicleCreate,
    VehicleResponse,
)
from app.vehicles.service import VehicleService

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)


def get_vehicle_service(
    db: AsyncSession = Depends(get_db),
) -> VehicleService:

    return VehicleService(
        VehicleRepository(db)
    )


@router.post(
    "/",
    response_model=VehicleResponse,
)
async def create_vehicle(
    payload: VehicleCreate,
    service: VehicleService = Depends(
        get_vehicle_service
    ),
    current_user: User = Depends(
        require_manager()
    ),
):

    return await service.create_vehicle(
        payload
    )


@router.get(
    "/",
    response_model=list[VehicleResponse],
)
async def list_vehicles(
    service: VehicleService = Depends(
        get_vehicle_service
    ),
):

    return await service.get_all()


@router.get(
    "/available",
    response_model=list[VehicleResponse],
)
async def available(
    service: VehicleService = Depends(
        get_vehicle_service
    ),
):

    return await service.available()