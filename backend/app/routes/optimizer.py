import time

from app.algorithms.shortest_path.dijkstra import Dijkstra
from app.algorithms.shortest_path.astar import AStar


class RouteOptimizer:

    def __init__(self, graph):

        self.graph = graph

    def solve(
        self,
        source,
        destination,
        algorithm="dijkstra",
    ):

        start = time.perf_counter()

        if algorithm.lower() == "astar":

            solver = AStar(self.graph)

        else:

            solver = Dijkstra(self.graph)

        result = solver.shortest_path(
            source,
            destination,
        )

        execution = (
            time.perf_counter()
            - start
        ) * 1000

        return {
            "algorithm": algorithm,
            "path": result["path"],
            "distance": result["distance"],
            "execution_time_ms": round(
                execution,
                3,
            ),
        }