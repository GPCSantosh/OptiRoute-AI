from fastapi import APIRouter

from app.simulation.vehicle_simulator import (
    vehicle_simulator,
)

from app.simulation.traffic_simulator import (
    traffic_simulator,
)

router = APIRouter(
    prefix="/simulation",
    tags=["Simulation"],
)


@router.get("/status")
def status():

    return {
        "vehicle_simulator": vehicle_simulator.running,
        "traffic_simulator": traffic_simulator.running,
        "vehicles": len(vehicle_simulator.vehicles),
        "roads": len(traffic_simulator.roads),
    }


@router.post("/start")
def start():

    vehicle_simulator.running = True

    traffic_simulator.running = True

    return {
        "status": "started"
    }


@router.post("/stop")
def stop():

    vehicle_simulator.stop()

    traffic_simulator.stop()

    return {
        "status": "stopped"
    }