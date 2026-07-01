from dataclasses import dataclass


@dataclass(slots=True)
class Node:

    id: str

    latitude: float

    longitude: float