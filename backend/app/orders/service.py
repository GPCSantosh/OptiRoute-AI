from sqlalchemy.ext.asyncio import AsyncSession

from app.orders.models import Order
from app.orders.repository import OrderRepository
from app.orders.schemas import (
    OrderCreate,
    OrderUpdate,
)


class OrderService:

    def __init__(self, db: AsyncSession):
        self.repository = OrderRepository(db)

    async def list_orders(self):
        return await self.repository.get_all()

    async def get_order(self, order_id):
        return await self.repository.get(order_id)

    async def create_order(
        self,
        payload: OrderCreate,
    ):
        order = Order(
            **payload.model_dump()
        )

        return await self.repository.create(order)

    async def update_order(
        self,
        order_id,
        payload: OrderUpdate,
    ):

        order = await self.repository.get(order_id)

        if order is None:
            return None

        data = payload.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(order, key, value)

        return await self.repository.update(order)

    async def delete_order(
        self,
        order_id,
    ):

        order = await self.repository.get(order_id)

        if order is None:
            return False

        await self.repository.delete(order)

        return True