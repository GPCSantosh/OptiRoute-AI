from pydantic import BaseModel


class RouteRequest(BaseModel):

    source: str

    destination: str

    algorithm: str = "dijkstra"


class RouteResponse(BaseModel):

    algorithm: str

    path: list[str]

    distance: float

    execution_time_ms: float