from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr

from app.drivers.models import DriverStatus


class DriverCreate(BaseModel):

    employee_id: str

    first_name: str

    last_name: str

    email: EmailStr

    phone: str

    license_number: str

    years_of_experience: int


class DriverUpdate(BaseModel):

    first_name: str | None = None

    last_name: str | None = None

    email: EmailStr | None = None

    phone: str | None = None

    status: DriverStatus | None = None

    rating: float | None = None

    is_available: bool | None = None


class DriverResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID

    employee_id: str

    first_name: str

    last_name: str

    email: EmailStr

    phone: str

    license_number: str

    years_of_experience: int

    rating: float

    completed_deliveries: int

    status: DriverStatus

    is_available: bool