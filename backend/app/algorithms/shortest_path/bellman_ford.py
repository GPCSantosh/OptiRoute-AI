from math import inf

from app.algorithms.graph.graph import Graph


class BellmanFord:

    """
    Time Complexity:
        O(VE)

    Space Complexity:
        O(V)
    """

    def __init__(
        self,
        graph: Graph,
    ):

        self.graph = graph

    def shortest_path(
        self,
        source: str,
    ):

        distance = {

            vertex: inf

            for vertex in self.graph.vertices()

        }

        distance[source] = 0

        previous = {}

        vertices = self.graph.vertices()

        edges = self.graph.edges()

        for _ in range(len(vertices) - 1):

            updated = False

            for edge in edges:

                if distance[edge.source] == inf:
                    continue

                weight = (
                    edge.distance
                    * edge.traffic_factor
                )

                if (

                    distance[edge.source]
                    + weight

                    < distance[edge.destination]

                ):

                    distance[
                        edge.destination
                    ] = (

                        distance[edge.source]
                        + weight

                    )

                    previous[
                        edge.destination
                    ] = edge.source

                    updated = True

            if not updated:
                break

        for edge in edges:

            weight = (
                edge.distance
                * edge.traffic_factor
            )

            if (
                distance[edge.source] + weight
                < distance[edge.destination]
            ):
                raise ValueError(
                    "Negative cycle detected."
                )

        return {

            "algorithm": "Bellman Ford",

            "distance": distance,

            "previous": previous,

        }