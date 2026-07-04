from __future__ import annotations

from sqlalchemy import DateTime
import enum
from datetime import datetime

from sqlalchemy import Boolean, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import BaseModel


class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    DISPATCHER = "DISPATCHER"
    DRIVER = "DRIVER"


class User(BaseModel):
    """
    System User
    """

    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.MANAGER,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )


    last_login = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    def __repr__(self):
        return (
            f"<User("
            f"id={self.id}, "
            f"username='{self.username}', "
            f"role='{self.role.value}'"
            f")>"
        )