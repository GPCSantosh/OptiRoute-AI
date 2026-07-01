from __future__ import annotations

import time
from math import inf

from app.algorithms.graph.graph import Graph
from app.algorithms.graph.priority_queue import PriorityQueue


class Dijkstra:

    """
    Dijkstra Shortest Path Algorithm

    Time Complexity:
        O((V + E) log V)

    Space Complexity:
        O(V)

    Supports:
        - Shortest path
        - Path reconstruction
        - Performance statistics
    """

    def __init__(
        self,
        graph: Graph,
    ):

        self.graph = graph

    def shortest_path(
        self,
        source: str,
        destination: str,
    ) -> dict:

        start = time.perf_counter()

        distances = {
            node: inf
            for node in self.graph.nodes
        }

        previous = {}

        visited = set()

        pq = PriorityQueue()

        distances[source] = 0

        pq.push(
            0,
            source,
        )

        expanded_nodes = 0

        while not pq.empty():

            current_distance, current = pq.pop()

            if current in visited:
                continue

            visited.add(current)

            expanded_nodes += 1

            if current == destination:
                break

            for edge in self.graph.neighbors(current):

                if edge.road_closed:
                    continue

                weight = (
                    edge.distance
                    * edge.traffic_factor
                )

                new_distance = (
                    current_distance + weight
                )

                if new_distance < distances[
                    edge.destination
                ]:

                    distances[
                        edge.destination
                    ] = new_distance

                    previous[
                        edge.destination
                    ] = current

                    pq.push(
                        new_distance,
                        edge.destination,
                    )

        execution_time = (
            time.perf_counter() - start
        ) * 1000

        path = self._reconstruct_path(
            previous,
            source,
            destination,
        )

        return {

            "algorithm": "Dijkstra",

            "distance": distances[
                destination
            ],

            "path": path,

            "visited_nodes": len(
                visited
            ),

            "expanded_nodes": expanded_nodes,

            "execution_time_ms": round(
                execution_time,
                4,
            ),
        }

    def _reconstruct_path(
        self,
        previous: dict,
        source: str,
        destination: str,
    ):

        if (
            destination != source
            and destination not in previous
        ):
            return []

        path = [destination]

        while path[-1] != source:

            path.append(
                previous[path[-1]]
            )

        path.reverse()

        return path