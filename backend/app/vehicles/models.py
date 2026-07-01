from __future__ import annotations

import enum

from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import BaseModel


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

    vehicle_name: Mapped[str] = mapped_column(
        String(100),
    )

    model: Mapped[str] = mapped_column(
        String(100),
    )

    manufacturer: Mapped[str] = mapped_column(
        String(100),
    )

    capacity_kg: Mapped[float] = mapped_column(
        Float,
    )

    fuel_capacity: Mapped[float] = mapped_column(
        Float,
    )

    current_fuel: Mapped[float] = mapped_column(
        Float,
    )

    mileage: Mapped[float] = mapped_column(
        Float,
    )

    max_speed: Mapped[int] = mapped_column(
        Integer,
    )

    fuel_type: Mapped[FuelType] = mapped_column(
        Enum(FuelType),
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

    from uuid import UUID

    from uuid import UUID

    driver_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("drivers.id"),
        nullable=True,
    )

    driver = relationship(
        "Driver",
        back_populates="vehicle",
        lazy="selectin",
    )

    def __repr__(self):

        return (
            f"<Vehicle("
            f"{self.registration_number}"
            f")>"
        )
    

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.vehicles.models import Vehicle


class Driver(BaseModel):

    __tablename__ = "drivers"

    # ... existing fields ...

    vehicle: Mapped["Vehicle | None"] = relationship(
        "Vehicle",
        back_populates="driver",
        uselist=False,
    )