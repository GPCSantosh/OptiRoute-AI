from __future__ import annotations

from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class Road(BaseModel):
    __tablename__ = "roads"

    road_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    source: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    destination: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    distance: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    travel_time: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    traffic_factor: Mapped[float] = mapped_column(
        Float,
        default=1.0,
    )

    closed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )