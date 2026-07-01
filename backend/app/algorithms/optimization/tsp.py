from app.algorithms.optimization.nearest_neighbor import NearestNeighbor
from app.algorithms.optimization.two_opt import TwoOpt


class TravelingSalesman:

    def __init__(self, graph):

        self.graph = graph

    def solve(
        self,
        start: str,
    ):

        nn = NearestNeighbor(
            self.graph
        )

        result = nn.solve(start)

        route = result["route"]

        if len(route) <= 2:

            return result

        distance_matrix = {}

        for source in self.graph.vertices():

            for edge in self.graph.neighbors(source):

                distance_matrix[
                    (
                        edge.source,
                        edge.destination,
                    )
                ] = edge.distance

        optimized = TwoOpt.optimize(
            route,
            distance_matrix,
        )

        result["route"] = optimized

        result["algorithm"] = "TSP + 2OPT"

        return result