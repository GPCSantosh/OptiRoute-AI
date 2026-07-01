from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import require_dispatcher
from app.db.session import get_db
from app.orders.repository import OrderRepository
from app.orders.schemas import (
    OrderCreate,
    OrderResponse,
)
from app.orders.service import OrderService
from app.users.models import User

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


def get_order_service(
    db: AsyncSession = Depends(get_db),
):

    return OrderService(
        OrderRepository(db)
    )


@router.post(
    "/",
    response_model=OrderResponse,
)
async def create(
    payload: OrderCreate,
    service: OrderService = Depends(
        get_order_service
    ),
    _: User = Depends(
        require_dispatcher()
    ),
):

    return await service.create(
        payload
    )


@router.get(
    "/",
    response_model=list[OrderResponse],
)
async def list_orders(
    service: OrderService = Depends(
        get_order_service
    ),
):

    return await service.all()