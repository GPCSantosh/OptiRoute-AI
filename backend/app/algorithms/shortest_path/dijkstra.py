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
    """

    def __init__(self, graph: Graph):
        self.graph = graph

    def shortest_path(
        self,
        source: str,
        destination: str,
    ) -> dict:

        source = source.strip()
        destination = destination.strip()

        # ----------------------------------
        # Validate Nodes
        # ----------------------------------

        print("\nSOURCE =", source)
        print("DESTINATION =", destination)

        print("\nAVAILABLE NODES")

        for n in self.graph.nodes:
            print("-", repr(n))

        if source not in self.graph.nodes:
            return {
                "algorithm": "Dijkstra",
                "distance": 0,
                "path": [],
                "visited_nodes": 0,
                "expanded_nodes": 0,
                "execution_time_ms": 0,
                "message": f"Source '{source}' not found.",
            }

        if destination not in self.graph.nodes:
            return {
                "algorithm": "Dijkstra",
                "distance": 0,
                "path": [],
                "visited_nodes": 0,
                "expanded_nodes": 0,
                "execution_time_ms": 0,
                "message": f"Destination '{destination}' not found.",
            }

        start = time.perf_counter()

        distances = {
            node: inf
            for node in self.graph.nodes
        }

        previous = {}

        visited = set()

        pq = PriorityQueue()
        if source not in distances:

            return {
                "algorithm": "Dijkstra",
                "success": False,
                "message": f"Unknown source '{source}'",
                "path": [],
            }

        if destination not in distances:

            return {
                "algorithm": "Dijkstra",
                "success": False,
                "message": f"Unknown destination '{destination}'",
                "path": [],
            }
        distances[source] = 0

        pq.push(
            0,
            source,
        )

        expanded_nodes = 0

        print("\nADJACENCY")

        for node in self.graph.adjacency:
            print(
                node,
                "->",
                [edge.destination for edge in self.graph.adjacency[node]]
            )
        # ----------------------------------
        # Main Loop
        # ----------------------------------

        while not pq.empty():

            current_distance, current = pq.pop()

            if current in visited:
                continue

            visited.add(current)

            expanded_nodes += 1

            if current == destination:
                break

            for edge in self.graph.neighbors(current):

                if edge.destination not in distances:
                    continue

                if edge.road_closed:
                    continue

                neighbor = edge.destination.strip()

                # Skip invalid nodes
                if neighbor not in distances:
                    continue

                weight = (
                    float(edge.distance)
                    * float(edge.traffic_factor)
                )

                new_distance = (
                    current_distance + weight
                )

                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance

                    previous[neighbor] = current

                    pq.push(
                        new_distance,
                        neighbor,
                    )

        execution_time = (
            time.perf_counter() - start
        ) * 1000

        # ----------------------------------
        # No Route Found
        # ----------------------------------

        if (
            destination != source
            and destination not in previous
        ):
            return {
                "algorithm": "Dijkstra",
                "distance": None,
                "path": [],
                "visited_nodes": len(visited),
                "expanded_nodes": expanded_nodes,
                "execution_time_ms": round(
                    execution_time,
                    4,
                ),
                "message": "No route found.",
            }

        # ----------------------------------
        # Reconstruct Path
        # ----------------------------------

        path = [destination]

        while path[-1] != source:
            path.append(
                previous[path[-1]]
            )

        path.reverse()

        return {
            "algorithm": "Dijkstra",
            "distance": round(
                distances[destination],
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