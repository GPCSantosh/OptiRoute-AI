from __future__ import annotations

from app.algorithms.graph.graph import Graph


class NearestNeighbor:
    """
    Greedy nearest-neighbor algorithm.

    Complexity:
        Time : O(n²)
        Space: O(n)
    """

    def __init__(
        self,
        graph: Graph,
    ):
        self.graph = graph

    def solve(
        self,
        start: str,
    ) -> dict:

        visited = {start}

        route = [start]

        total_distance = 0.0

        current = start

        while len(visited) < len(self.graph):

            nearest = None

            minimum = float("inf")

            for edge in self.graph.neighbors(current):

                if edge.destination in visited:
                    continue

                weight = (
                    edge.distance
                    * edge.traffic_factor
                )

                if weight < minimum:

                    minimum = weight

                    nearest = edge

            if nearest is None:
                break

            visited.add(
                nearest.destination
            )

            route.append(
                nearest.destination
            )

            total_distance += minimum

            current = nearest.destination

        return {

            "algorithm": "Nearest Neighbor",

            "route": route,

            "distance": round(
                total_distance,
                2,
            ),

            "visited": len(visited),
        }