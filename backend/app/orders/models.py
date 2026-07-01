from __future__ import annotations

import enum
from uuid import UUID

from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import BaseModel


class OrderPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"


class OrderStatus(str, enum.Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class Order(BaseModel):

    __tablename__ = "orders"

    order_number: Mapped[str] = mapped_column(
        String(40),
        unique=True,
        nullable=False,
        index=True,
    )

    customer_name: Mapped[str] = mapped_column(
        String(150)
    )

    customer_phone: Mapped[str] = mapped_column(
        String(20)
    )

    pickup_address: Mapped[str] = mapped_column(
        String(255)
    )

    delivery_address: Mapped[str] = mapped_column(
        String(255)
    )

    pickup_latitude: Mapped[float] = mapped_column(
        Float
    )

    pickup_longitude: Mapped[float] = mapped_column(
        Float
    )

    delivery_latitude: Mapped[float] = mapped_column(
        Float
    )

    delivery_longitude: Mapped[float] = mapped_column(
        Float
    )

    package_weight: Mapped[float] = mapped_column(
        Float
    )

    estimated_distance: Mapped[float] = mapped_column(
        Float,
        default=0
    )

    estimated_time: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    priority: Mapped[OrderPriority] = mapped_column(
        Enum(OrderPriority),
        default=OrderPriority.MEDIUM,
    )

    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus),
        default=OrderStatus.PENDING,
    )

    warehouse_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("warehouses.id"),
        nullable=True,
    )

    driver_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("drivers.id"),
        nullable=True,
    )

    vehicle_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("vehicles.id"),
        nullable=True,
    )

    warehouse = relationship(
        "Warehouse",
        lazy="selectin",
    )

    driver = relationship(
        "Driver",
        lazy="selectin",
    )

    vehicle = relationship(
        "Vehicle",
        lazy="selectin",
    )