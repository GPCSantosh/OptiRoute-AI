from fastapi import APIRouter

from app.simulation.vehicle_simulator import (
    vehicle_simulator,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/dashboard")
def dashboard():

    vehicles = list(
        vehicle_simulator.vehicles.values()
    )

    total = len(vehicles)

    moving = len(
        [
            v
            for v in vehicles
            if v["status"] == "MOVING"
        ]
    )

    avg_fuel = (
        sum(
            v["fuel"]
            for v in vehicles
        )
        / total
        if total
        else 0
    )

    avg_speed = (
        sum(
            v["speed"]
            for v in vehicles
        )
        / total
        if total
        else 0
    )

    return {
        "vehicles": total,
        "moving": moving,
        "average_speed": round(
            avg_speed,
            2,
        ),
        "average_fuel": round(
            avg_fuel,
            2,
        ),
    }