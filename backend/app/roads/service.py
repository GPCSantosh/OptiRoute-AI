from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions.base import NotFoundException
from app.roads.models import Road
from app.roads.repository import RoadRepository
from app.roads.schemas import (
    RoadCreate,
    RoadUpdate,
)


class RoadService:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.repository = RoadRepository(db)

    # ------------------------------------------
    # Get All Roads
    # ------------------------------------------

    async def get_roads(self):
        return await self.repository.get_all()

    # ------------------------------------------
    # Get Road
    # ------------------------------------------

    async def get_road(
        self,
        road_id: UUID,
    ):
        road = await self.repository.get(
            road_id
        )

        if road is None:
            raise NotFoundException(
                "Road not found."
            )

        return road

    # ------------------------------------------
    # Create Road
    # ------------------------------------------

    async def create_road(
        self,
        payload: RoadCreate,
    ):

        road = Road(
            road_name=payload.road_name,
            source=payload.source,
            destination=payload.destination,
            distance=payload.distance,
            travel_time=payload.travel_time,
            traffic_factor=1.0,
            closed=False,
        )

        return await self.repository.create(
            road
        )

    # ------------------------------------------
    # Update Road
    # ------------------------------------------

    async def update_road(
        self,
        road_id: UUID,
        payload: RoadUpdate,
    ):

        road = await self.repository.get(
            road_id
        )

        if road is None:
            raise NotFoundException(
                "Road not found."
            )

        road.road_name = payload.road_name
        road.source = payload.source
        road.destination = payload.destination
        road.distance = payload.distance
        road.travel_time = payload.travel_time
        road.traffic_factor = payload.traffic_factor
        road.closed = payload.closed

        return await self.repository.update(
            road
        )

    # ------------------------------------------
    # Delete Road
    # ------------------------------------------

    async def delete_road(
        self,
        road_id: UUID,
    ):

        road = await self.repository.get(
            road_id
        )

        if road is None:
            raise NotFoundException(
                "Road not found."
            )

        await self.repository.delete(
            road
        )

        return {
            "message": "Road deleted successfully."
        }