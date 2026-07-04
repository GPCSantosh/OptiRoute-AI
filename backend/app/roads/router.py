from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.roads.schemas import (
    RoadCreate,
    RoadResponse,
    RoadUpdate,
)
from app.roads.service import RoadService

router = APIRouter(
    prefix="/roads",
    tags=["Roads"],
)


# ------------------------------------------
# Get All Roads
# ------------------------------------------

@router.get(
    "/",
    response_model=list[RoadResponse],
)
async def get_roads(
    db: AsyncSession = Depends(get_db),
):
    return await RoadService(db).get_roads()


# ------------------------------------------
# Get Road
# ------------------------------------------

@router.get(
    "/{road_id}",
    response_model=RoadResponse,
)
async def get_road(
    road_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await RoadService(db).get_road(
        road_id
    )


# ------------------------------------------
# Create Road
# ------------------------------------------

@router.post(
    "/",
    response_model=RoadResponse,
)
async def create_road(
    payload: RoadCreate,
    db: AsyncSession = Depends(get_db),
):
    return await RoadService(db).create_road(
        payload
    )


# ------------------------------------------
# Update Road
# ------------------------------------------

@router.put(
    "/{road_id}",
    response_model=RoadResponse,
)
async def update_road(
    road_id: UUID,
    payload: RoadUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await RoadService(db).update_road(
        road_id,
        payload,
    )


# ------------------------------------------
# Delete Road
# ------------------------------------------

@router.delete(
    "/{road_id}",
)
async def delete_road(
    road_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await RoadService(db).delete_road(
        road_id
    )