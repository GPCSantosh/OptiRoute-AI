from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.orders.schemas import (
    OrderCreate,
    OrderResponse,
    OrderUpdate,
)
from app.orders.service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.get("/", response_model=list[OrderResponse])
async def list_orders(
    db: AsyncSession = Depends(get_db),
):
    return await OrderService(db).list_orders()


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id,
    db: AsyncSession = Depends(get_db),
):
    return await OrderService(db).get_order(order_id)


@router.post("/", response_model=OrderResponse)
async def create_order(
    payload: OrderCreate,
    db: AsyncSession = Depends(get_db),
):
    return await OrderService(db).create_order(payload)


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(
    order_id,
    payload: OrderUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await OrderService(db).update_order(
        order_id,
        payload,
    )


@router.delete("/{order_id}")
async def delete_order(
    order_id,
    db: AsyncSession = Depends(get_db),
):
    success = await OrderService(db).delete_order(order_id)

    return {"success": success}