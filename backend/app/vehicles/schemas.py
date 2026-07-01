from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict

from app.vehicles.models import (
    FuelType,
    VehicleStatus,
)


class VehicleCreate(BaseModel):

    registration_number: str

    vehicle_name: str

    manufacturer: str

    model: str

    capacity_kg: float

    fuel_capacity: float

    current_fuel: float

    mileage: float

    max_speed: int

    fuel_type: FuelType


class VehicleUpdate(BaseModel):

    current_fuel: float | None = None

    status: VehicleStatus | None = None

    is_available: bool | None = None


class VehicleResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    registration_number: str

    vehicle_name: str

    manufacturer: str

    model: str

    capacity_kg: float

    fuel_capacity: float

    current_fuel: float

    mileage: float

    max_speed: int

    fuel_type: FuelType

    status: VehicleStatus