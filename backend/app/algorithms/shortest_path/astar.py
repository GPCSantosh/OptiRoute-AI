from __future__ import annotations

import math
import time
from math import inf

from app.algorithms.graph.graph import Graph
from app.algorithms.graph.priority_queue import PriorityQueue


class AStar:
    """
    A* Shortest Path Algorithm

    Improvements
    -----------------------
    ✓ Safe node validation
    ✓ No KeyError
    ✓ Handles missing coordinates
    ✓ Ignores closed roads
    ✓ Returns friendly errors
    """

    def __init__(self, graph: Graph):
        self.graph = graph

    def heuristic(
        self,
        source: str,
        destination: str,
    ) -> float:

        source = source.strip()
        destination = destination.strip()

        source_node = self.graph.get_node(source)
        destination_node = self.graph.get_node(destination)

        if source_node is None or destination_node is None:
            return 0

        # Missing coordinates
        if (
            source_node.latitude == 0
            and source_node.longitude == 0
        ):
            return 0

        if (
            destination_node.latitude == 0
            and destination_node.longitude == 0
        ):
            return 0

        return math.sqrt(
            (source_node.latitude - destination_node.latitude) ** 2
            +
            (source_node.longitude - destination_node.longitude) ** 2
        )

    def shortest_path(
        self,
        source: str,
        destination: str,
    ):

        source = source.strip()
        destination = destination.strip()

        if source not in self.graph.nodes:

            return {
                "algorithm": "A*",
                "distance": 0,
                "path": [],
                "visited_nodes": 0,
                "expanded_nodes": 0,
                "execution_time_ms": 0,
                "message": f"Source '{source}' not found.",
            }

        if destination not in self.graph.nodes:

            return {
                "algorithm": "A*",
                "distance": 0,
                "path": [],
                "visited_nodes": 0,
                "expanded_nodes": 0,
                "execution_time_ms": 0,
                "message": f"Destination '{destination}' not found.",
            }

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

                neighbor = edge.destination.strip()

                if neighbor not in g_score:
                    continue

                tentative_g = (
                    g_score[current]
                    + (
                        float(edge.distance)
                        * float(edge.traffic_factor)
                    )
                )

                if tentative_g < g_score[neighbor]:

                    previous[neighbor] = current

                    g_score[neighbor] = tentative_g

                    f_score[neighbor] = (
                        tentative_g
                        + self.heuristic(
                            neighbor,
                            destination,
                        )
                    )

                    pq.push(
                        f_score[neighbor],
                        neighbor,
                    )

        execution_time = (
            time.perf_counter() - start
        ) * 1000

        if (
            destination != source
            and destination not in previous
        ):

            return {
                "algorithm": "A*",
                "distance": 0,
                "path": [],
                "visited_nodes": len(visited),
                "expanded_nodes": expanded_nodes,
                "execution_time_ms": round(
                    execution_time,
                    4,
                ),
                "message": "No route found.",
            }

        path = [destination]

        while path[-1] != source:

            path.append(
                previous[path[-1]]
            )

        path.reverse()

        return {
            "algorithm": "A*",
            "distance": round(
                g_score[destination],
                2,
            ),
            "path": path,
            "visited_nodes": len(visited),
            "expanded_nodes": expanded_nodes,
            "execution_time_ms": round(
                execution_time,
                4,
            ),
        }