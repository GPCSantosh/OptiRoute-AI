from __future__ import annotations

import time
from math import inf

from app.algorithms.graph.graph import Graph
from app.algorithms.graph.priority_queue import PriorityQueue
from app.algorithms.graph.utils import haversine


class AStar:
    """
    A* Shortest Path Algorithm

    Time Complexity:
        Worst: O((V + E) log V)
        Best: Much faster than Dijkstra

    Space Complexity:
        O(V)
    """

    def __init__(
        self,
        graph: Graph,
    ):
        self.graph = graph

    def heuristic(
        self,
        current: str,
        destination: str,
    ) -> float:

        current_node = self.graph.get_node(current)
        destination_node = self.graph.get_node(destination)

        return haversine(
            current_node.latitude,
            current_node.longitude,
            destination_node.latitude,
            destination_node.longitude,
        )

    def shortest_path(
        self,
        source: str,
        destination: str,
    ) -> dict:

        start = time.perf_counter()

        g_score = {
            node: inf
            for node in self.graph.nodes
        }

        f_score = {
            node: inf
            for node in self.graph.nodes
        }

        previous = {}

        visited = set()

        pq = PriorityQueue()

        g_score[source] = 0

        f_score[source] = self.heuristic(
            source,
            destination,
        )

        pq.push(
            f_score[source],
            source,
        )

        expanded_nodes = 0

        while not pq.empty():

            _, current = pq.pop()

            if current in visited:
                continue

            visited.add(current)

            expanded_nodes += 1

            if current == destination:
                break

            for edge in self.graph.neighbors(current):

                if edge.road_closed:
                    continue

                tentative_g = (
                    g_score[current]
                    + edge.distance * edge.traffic_factor
                )

                if tentative_g < g_score[edge.destination]:

                    previous[edge.destination] = current

                    g_score[edge.destination] = tentative_g

                    f_score[edge.destination] = (
                        tentative_g
                        + self.heuristic(
                            edge.destination,
                            destination,
                        )
                    )

                    pq.push(
                        f_score[edge.destination],
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
            "algorithm": "A*",
            "distance": g_score[destination],
            "path": path,
            "visited_nodes": len(visited),
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