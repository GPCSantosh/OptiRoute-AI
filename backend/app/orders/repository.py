from sqlalchemy import select

from app.orders.models import Order
from app.repositories.base import BaseRepository


class OrderRepository(
    BaseRepository[Order]
):

    def __init__(self, db):

        super().__init__(
            Order,
            db,
        )

    async def get_by_order_number(
        self,
        number: str,
    ):

        result = await self.db.execute(
            select(Order).where(
                Order.order_number == number
            )
        )

        return result.scalar_one_or_none()