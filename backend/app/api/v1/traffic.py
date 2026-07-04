from fastapi import APIRouter

from app.simulation.traffic_simulator import traffic_simulator

router = APIRouter(
    prefix="/traffic",
    tags=["Traffic"],
)


@router.get("/")
def list_roads():

    return list(
        traffic_simulator.roads.values()
    )


@router.get("/{road_id}")
def get_road(
    road_id: int,
):

    return traffic_simulator.roads.get(
        road_id
    )


@router.post("/{road_id}/close")
def close_road(
    road_id: int,
):

    if road_id not in traffic_simulator.roads:

        return {
            "success": False
        }

    traffic_simulator.roads[
        road_id
    ]["closed"] = True

    return {
        "success": True
    }


@router.post("/{road_id}/open")
def open_road(
    road_id: int,
):

    if road_id not in traffic_simulator.roads:

        return {
            "success": False
        }

    traffic_simulator.roads[
        road_id
    ]["closed"] = False

    return {
        "success": True
    }