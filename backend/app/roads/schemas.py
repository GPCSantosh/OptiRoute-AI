from uuid import UUID
from pydantic import BaseModel

class RoadCreate(BaseModel):
    road_name: str
    source: str
    destination: str
    distance: float
    travel_time: int


class RoadUpdate(BaseModel):
    road_name: str
    source: str
    destination: str
    distance: float
    travel_time: int
    traffic_factor: float
    closed: bool


class RoadResponse(BaseModel):
    id: UUID
    road_name: str
    source: str
    destination: str
    distance: float
    travel_time: int
    traffic_factor: float
    closed: bool

    class Config:
        from_attributes = True