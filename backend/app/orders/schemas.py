from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict

from app.orders.models import (
    OrderPriority,
    OrderStatus,
)


class OrderCreate(BaseModel):

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


class OrderResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    order_number: str

    customer_name: str

    customer_phone: str

    status: OrderStatus

    priority: OrderPriority

    package_weight: float

    estimated_distance: float

    estimated_time: int