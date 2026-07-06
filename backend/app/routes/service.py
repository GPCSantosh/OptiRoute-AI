from sqlalchemy.ext.asyncio import AsyncSession

from app.algorithms.services.graph_builder import GraphBuilder
from app.roads.repository import RoadRepository
from app.routes.optimizer import RouteOptimizer
from app.warehouses.repository import WarehouseRepository


class RouteService:
    """
    Route Optimization Service
    Builds the graph dynamically from the database.
    """

    def __init__(self, db: AsyncSession):
        self.db = db
        self.road_repository = RoadRepository(db)
        self.warehouse_repository = WarehouseRepository(db)

    async def optimize(self, payload):

        # Load data from database
        warehouses = await self.warehouse_repository.get_all()
        roads = await self.road_repository.get_all()

        warehouses = await self.warehouse_repository.get_all()
        roads = await self.road_repository.get_all()

        print("\nWAREHOUSES FROM DB")
        for w in warehouses:
            print(w.city)

        print("\nROADS FROM DB")
        for r in roads:
            print(r.source, "->", r.destination)
        # Build graph
        graph = GraphBuilder.build(
            warehouses,
            roads,
        )

        # Create optimizer
        optimizer = RouteOptimizer(graph)

        # Run algorithm
        return optimizer.solve(
            payload.source,
            payload.destination,
            payload.algorithm,
        )