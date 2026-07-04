from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.routes.schemas import RouteRequest, RouteResponse
from app.routes.service import RouteService

router = APIRouter(
    prefix="/routes",
    tags=["Route Optimization"],
)


@router.post(
    "/optimize",
    response_model=RouteResponse,
)
async def optimize(
    payload: RouteRequest,
    db: AsyncSession = Depends(get_db),
):
    return await RouteService(db).optimize(payload)