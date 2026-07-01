from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import BaseModel


class Warehouse(BaseModel):

    __tablename__ = "warehouses"

    warehouse_code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    warehouse_name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    address: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    state: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    total_capacity: Mapped[int] = mapped_column(
        Integer,
        default=10000,
    )

    available_capacity: Mapped[int] = mapped_column(
        Integer,
        default=10000,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    def __repr__(self):

        return (
            f"<Warehouse("
            f"{self.warehouse_code}"
            f")>"
        )