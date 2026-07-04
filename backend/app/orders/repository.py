from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.orders.models import Order


class OrderRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    from uuid import UUID

    async def get(
        self,
        order_id: UUID,
    ):
        result = await self.db.execute(
            select(Order).where(
                Order.id == order_id
            )
        )

        return result.scalar_one_or_none()

    async def update(
        self,
        order: Order,
    ):
        self.db.add(order)

        await self.db.commit()

        await self.db.refresh(order)

        return order

    async def get_all(self):

        result = await self.db.execute(
            select(Order)
        )

        return result.scalars().all()

    async def get_by_id(self, order_id):

        result = await self.db.execute(
            select(Order).where(
                Order.id == order_id
            )
        )

        return result.scalar_one_or_none()
    async def delete(
        self,
        order: Order,
    ):
        await self.db.delete(order)
        await self.db.commit()

    async def create(self, order):

        self.db.add(order)

        await self.db.commit()

        await self.db.refresh(order)

        return order