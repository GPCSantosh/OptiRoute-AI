from app.algorithms.graph.graph import Graph

from app.algorithms.optimization.vrp import (

    VehicleRoutingProblem,

)

from app.algorithms.shortest_path.astar import AStar

from app.algorithms.shortest_path.dijkstra import Dijkstra


class RouteOptimizer:

    """
    High-Level Optimization Service

    This is the ONLY class

    that APIs should call.
    """

    def __init__(

        self,

        graph: Graph,

    ):

        self.graph = graph

        self.dijkstra = Dijkstra(graph)

        self.astar = AStar(graph)

        self.vrp = VehicleRoutingProblem(graph)

    def shortest_route(

        self,

        source,

        destination,

        algorithm="astar",

    ):

        if algorithm.lower() == "dijkstra":

            return self.dijkstra.shortest_path(

                source,

                destination,

            )

        return self.astar.shortest_path(

            source,

            destination,

        )

    def fleet_optimization(

        self,

        warehouse,

        vehicles,

        drivers,

        orders,

    ):

        return self.vrp.optimize(

            warehouse,

            vehicles,

            drivers,

            orders,

        )