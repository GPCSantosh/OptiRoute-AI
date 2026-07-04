from fastapi import APIRouter

from app.simulation.vehicle_simulator import vehicle_simulator
from app.simulation.traffic_simulator import traffic_simulator

router = APIRouter(
    prefix="/tracking",
    tags=["Tracking"],
)


@router.get("/vehicles")
def vehicles():

    return list(
        vehicle_simulator.vehicles.values()
    )


@router.get("/traffic")
def traffic():

    return list(
        traffic_simulator.roads.values()
    )