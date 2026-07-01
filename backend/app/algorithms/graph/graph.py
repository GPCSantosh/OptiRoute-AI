from __future__ import annotations

from collections import defaultdict

from app.algorithms.graph.edge import Edge
from app.algorithms.graph.node import Node


class Graph:
    """
    Generic weighted graph.

    Supports:
        • Directed Graphs
        • Undirected Graphs
        • Weighted Edges
        • Traffic Multipliers
        • Closed Roads

    Used by:
        • Dijkstra
        • A*
        • Bellman-Ford
        • Floyd-Warshall
        • Prim
        • Kruskal
        • TSP
        • VRP
    """

    def __init__(
        self,
        directed: bool = False,
    ):

        self.directed = directed

        self.nodes: dict[str, Node] = {}

        self.adjacency: dict[str, list[Edge]] = defaultdict(list)

    # -------------------------------------------------

    def add_node(
        self,
        node: Node,
    ) -> None:

        self.nodes[node.id] = node

    # -------------------------------------------------

    def add_edge(
        self,
        edge: Edge,
    ) -> None:

        self.adjacency[
            edge.source
        ].append(edge)

        if not self.directed:

            reverse = Edge(
                source=edge.destination,
                destination=edge.source,
                distance=edge.distance,
                travel_time=edge.travel_time,
                traffic_factor=edge.traffic_factor,
                road_closed=edge.road_closed,
                road_name=edge.road_name,
            )

            self.adjacency[
                edge.destination
            ].append(reverse)

    # -------------------------------------------------

    def remove_edge(
        self,
        source: str,
        destination: str,
    ) -> None:

        self.adjacency[source] = [

            edge

            for edge in self.adjacency[source]

            if edge.destination != destination

        ]

        if not self.directed:

            self.adjacency[destination] = [

                edge

                for edge in self.adjacency[destination]

                if edge.destination != source

            ]

    # -------------------------------------------------

    def neighbors(
        self,
        node: str,
    ) -> list[Edge]:

        return self.adjacency[node]

    # -------------------------------------------------

    def edges(self) -> list[Edge]:

        if self.directed:

            edges = []

            for edge_list in self.adjacency.values():
                edges.extend(edge_list)

            return edges

        visited = set()

        unique = []

        for edge_list in self.adjacency.values():

            for edge in edge_list:

                key = tuple(
                    sorted(
                        (
                            edge.source,
                            edge.destination,
                        )
                    )
                )

                if key in visited:
                    continue

                visited.add(key)

                unique.append(edge)

        return unique

    # -------------------------------------------------

    def vertices(self):

        return list(
            self.nodes.keys()
        )

    # -------------------------------------------------

    def get_node(
        self,
        node: str,
    ) -> Node:

        return self.nodes[node]

    # -------------------------------------------------

    def has_node(
        self,
        node: str,
    ) -> bool:

        return node in self.nodes

    # -------------------------------------------------

    def clear(self):

        self.nodes.clear()

        self.adjacency.clear()

    # -------------------------------------------------

    def __len__(self):

        return len(
            self.nodes
        )

    # -------------------------------------------------

    def __contains__(
        self,
        node: str,
    ):

        return node in self.nodes

    # -------------------------------------------------

    def __repr__(self):

        return (
            f"Graph("
            f"nodes={len(self.nodes)}, "
            f"edges={len(self.edges())}, "
            f"directed={self.directed})"
        )