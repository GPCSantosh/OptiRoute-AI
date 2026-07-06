from app.algorithms.graph.edge import Edge
from app.algorithms.graph.graph import Graph
from app.algorithms.graph.node import Node

class GraphBuilder:

    @staticmethod
    def build(warehouses, roads):

        graph = Graph()

        print("\n========== BUILD GRAPH ==========")

        for warehouse in warehouses:

            print(
                "NODE:",
                warehouse.city,
                warehouse.latitude,
                warehouse.longitude,
            )

            graph.add_node(
                Node(
                    warehouse.city.strip(),
                    warehouse.latitude,
                    warehouse.longitude,
                )
            )
        print("Nodes:", list(graph.nodes.keys()))

        for node, edges in graph.adjacency.items():
            print(node)
            for edge in edges:
                print(f"  -> {edge.destination} ({edge.distance})")

        print("\n----- ROADS -----")

        for road in roads:

            print(
                road.source,
                "---->",
                road.destination,
            )

            graph.add_edge(
                Edge(
                    source=road.source.strip(),
                    destination=road.destination.strip(),
                    distance=road.distance,
                    travel_time=road.travel_time,
                    traffic_factor=road.traffic_factor,
                    road_closed=road.closed,
                    road_name=road.road_name,
                )
            )

        print("\nGRAPH NODES")
        print(graph.nodes.keys())

        print("\nGRAPH ADJACENCY")

        for node in graph.adjacency:

            print(
                node,
                "=>",
                [
                    e.destination
                    for e in graph.adjacency[node]
                ],
            )

        print("=============================\n")

        return graph