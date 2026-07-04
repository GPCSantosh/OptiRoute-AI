from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict

from app.orders.models import (
    OrderPriority,
    OrderStatus,
)


class OrderBase(BaseModel):

    order_number: str

    customer_name: str

    customer_phone: str

    pickup_address: str

    delivery_address: str

    pickup_latitude: float

    pickup_longitude: float

    delivery_latitude: float

    delivery_longitude: float

    package_weight: float

    priority: OrderPriority = OrderPriority.MEDIUM


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):

    customer_name: str | None = None

    customer_phone: str | None = None

    pickup_address: str | None = None

    delivery_address: str | None = None

    pickup_latitude: float | None = None

    pickup_longitude: float | None = None

    delivery_latitude: float | None = None

    delivery_longitude: float | None = None

    package_weight: float | None = None

    priority: OrderPriority | None = None

    status: OrderStatus | None = None


class OrderResponse(OrderBase):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    estimated_distance: float

    estimated_time: int

    status: OrderStatus