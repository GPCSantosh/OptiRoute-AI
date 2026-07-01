from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2

from app.exceptions.base import ConflictException
from app.warehouses.models import Warehouse
from app.warehouses.repository import WarehouseRepository
from app.warehouses.schemas import WarehouseCreate


class WarehouseService:

    def __init__(
        self,
        repository: WarehouseRepository,
    ):

        self.repository = repository

    async def create(
        self,
        payload: WarehouseCreate,
    ):

        warehouse = await self.repository.get_by_code(
            payload.warehouse_code
        )

        if warehouse:

            raise ConflictException(
                "Warehouse code already exists."
            )

        warehouse = Warehouse(
            **payload.model_dump(),
            available_capacity=payload.total_capacity,
        )

        return await self.repository.create(
            warehouse
        )

    async def all(self):

        return await self.repository.get_all()

    async def active(self):

        return await self.repository.active_warehouses()

    @staticmethod
    def haversine(
        lat1,
        lon1,
        lat2,
        lon2,
    ):

        R = 6371

        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)

        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1))
            * cos(radians(lat2))
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a),
        )

        return R * c

    async def nearest_warehouse(
        self,
        latitude: float,
        longitude: float,
    ):

        warehouses = await self.repository.active_warehouses()

        nearest = None

        minimum = float("inf")

        for warehouse in warehouses:

            distance = self.haversine(
                latitude,
                longitude,
                warehouse.latitude,
                warehouse.longitude,
            )

            if distance < minimum:

                minimum = distance

                nearest = warehouse

        return nearest