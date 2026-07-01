from __future__ import annotations

import enum

from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import BaseModel


class DriverStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"

    ON_DELIVERY = "ON_DELIVERY"

    OFFLINE = "OFFLINE"

    ON_BREAK = "ON_BREAK"

    LEAVE = "LEAVE"


class Driver(BaseModel):

    __tablename__ = "drivers"

    employee_id: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    license_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    years_of_experience: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    rating: Mapped[float] = mapped_column(
        Float,
        default=5.0,
    )

    completed_deliveries: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    current_latitude: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    current_longitude: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    status: Mapped[DriverStatus] = mapped_column(
        Enum(DriverStatus),
        default=DriverStatus.AVAILABLE,
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    def __repr__(self):

        return (
            f"<Driver("
            f"{self.employee_id}, "
            f"{self.first_name} "
            f"{self.last_name}"
            f")>"
        )