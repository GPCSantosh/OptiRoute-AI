from pydantic import BaseModel


class VehicleLocation(BaseModel):

    vehicle_id: int

    latitude: float

    longitude: float

    speed: float

    fuel: float

    eta: int

    status: str


class TrafficUpdate(BaseModel):

    road_id: int

    traffic_level: int

    speed_limit: int

    closed: bool

    weather: str