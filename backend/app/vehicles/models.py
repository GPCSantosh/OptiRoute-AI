from __future__ import annotations

import enum
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    Boolean,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.base import BaseModel

if TYPE_CHECKING:
    from app.drivers.models import Driver


class VehicleStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    IN_USE = "IN_USE"
    MAINTENANCE = "MAINTENANCE"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"


class FuelType(str, enum.Enum):
    PETROL = "PETROL"
    DIESEL = "DIESEL"
    ELECTRIC = "ELECTRIC"
    HYBRID = "HYBRID"


class Vehicle(BaseModel):
    __tablename__ = "vehicles"

    registration_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    vehicle_name: Mapped[str] = mapped_column(String(100))

    model: Mapped[str] = mapped_column(String(100))

    manufacturer: Mapped[str] = mapped_column(String(100))

    capacity_kg: Mapped[float] = mapped_column(Float)

    fuel_capacity: Mapped[float] = mapped_column(Float)

    current_fuel: Mapped[float] = mapped_column(Float)

    mileage: Mapped[float] = mapped_column(Float)

    max_speed: Mapped[int] = mapped_column(Integer)

    fuel_type: Mapped[FuelType] = mapped_column(
        Enum(FuelType)
    )

    status: Mapped[VehicleStatus] = mapped_column(
        Enum(VehicleStatus),
        default=VehicleStatus.AVAILABLE,
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    current_latitude: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    current_longitude: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    driver_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("drivers.id"),
        nullable=True,
    )

    driver: Mapped["Driver | None"] = relationship(
        "Driver",
        back_populates="vehicle",
        lazy="selectin",
    )

    def __repr__(self):
        return f"<Vehicle {self.registration_number}>"