from dataclasses import dataclass


@dataclass(slots=True)
class Edge:

    source: str

    destination: str

    distance: float

    travel_time: float

    traffic_factor: float = 1.0

    road_closed: bool = False

    road_name: str = ""