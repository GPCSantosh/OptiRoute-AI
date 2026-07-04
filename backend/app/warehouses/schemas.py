from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict


class WarehouseCreate(BaseModel):
    warehouse_code: str
    warehouse_name: str
    address: str
    city: str
    state: str
    latitude: float
    longitude: float
    total_capacity: int = 10000
    available_capacity: int | None = None
    is_active: bool = True


class WarehouseUpdate(BaseModel):

    warehouse_name: str | None = None

    address: str | None = None

    city: str | None = None

    state: str | None = None

    available_capacity: int | None = None

    is_active: bool | None = None


class WarehouseResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    warehouse_code: str

    warehouse_name: str

    address: str

    city: str

    state: str

    latitude: float

    longitude: float

    total_capacity: int

    available_capacity: int

    is_active: bool