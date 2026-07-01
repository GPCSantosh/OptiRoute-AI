from app.exceptions.base import ConflictException
from app.orders.models import Order
from app.orders.repository import OrderRepository
from app.orders.schemas import OrderCreate


class OrderService:

    def __init__(
        self,
        repository: OrderRepository,
    ):

        self.repository = repository

    async def create(
        self,
        payload: OrderCreate,
    ):

        existing = await self.repository.get_by_order_number(
            payload.order_number
        )

        if existing:

            raise ConflictException(
                "Order already exists."
            )

        order = Order(
            **payload.model_dump()
        )

        return await self.repository.create(
            order
        )

    async def all(self):

        return await self.repository.get_all()