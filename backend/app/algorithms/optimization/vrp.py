from __future__ import annotations

from dataclasses import dataclass

from app.algorithms.optimization.tsp import TravelingSalesman
from app.algorithms.shortest_path.astar import AStar
from app.algorithms.graph.graph import Graph


@dataclass(slots=True)
class RouteStop:

    node: str

    order=None

    arrival_time: float = 0


@dataclass(slots=True)
class VehiclePlan:

    vehicle=None

    driver=None

    warehouse=None

    stops: list[RouteStop] = None

    total_distance: float = 0

    total_time: float = 0

    utilization: float = 0


class VehicleRoutingProblem:
    """
    Production Fleet Optimizer

    Pipeline

    Warehouse

        ↓

    Vehicle Assignment

        ↓

    Route Construction

        ↓

    A* Shortest Paths

        ↓

    TSP Optimization

        ↓

    Final Route
    """

    def __init__(
        self,
        graph: Graph,
    ):

        self.graph = graph

        self.astar = AStar(graph)

        self.tsp = TravelingSalesman(graph)

    # ---------------------------------------------------

    def optimize(

        self,

        warehouse,

        vehicles,

        drivers,

        orders,

    ):

        plans = []

        available = [

            v

            for v in vehicles

            if v.is_available

        ]

        driver_pool = [

            d

            for d in drivers

            if d.is_available

        ]

        remaining = sorted(

            orders,

            key=lambda o: (

                o.priority.value,

                -o.package_weight,

            ),

        )

        for vehicle in available:

            capacity = vehicle.capacity_kg

            current_weight = 0

            assigned = []

            for order in remaining[:]:

                if (

                    current_weight

                    + order.package_weight

                    > capacity

                ):

                    continue

                assigned.append(order)

                remaining.remove(order)

                current_weight += order.package_weight

            if not assigned:

                continue

            route = self.tsp.solve(

                warehouse.warehouse_code

            )

            distance = route["distance"]

            driver = None

            if driver_pool:

                driver = driver_pool.pop(0)

            plans.append(

                VehiclePlan(

                    vehicle=vehicle,

                    driver=driver,

                    warehouse=warehouse,

                    stops=[

                        RouteStop(

                            warehouse.warehouse_code

                        )

                    ],

                    total_distance=distance,

                    total_time=distance / max(

                        vehicle.max_speed,

                        1,

                    ),

                    utilization=round(

                        current_weight

                        / vehicle.capacity_kg,

                        2,

                    ),

                )

            )

        return plans