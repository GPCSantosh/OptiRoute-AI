from app.algorithms.graph.edge import Edge
from app.algorithms.graph.graph import Graph
from app.algorithms.graph.node import Node


class GraphBuilder:
    """
    Builds graph from database objects.
    """

    @staticmethod
    def build(

        warehouses,

        roads,

    ) -> Graph:

        graph = Graph()

        for warehouse in warehouses:

            graph.add_node(

                Node(

                    warehouse.warehouse_code,

                    warehouse.latitude,

                    warehouse.longitude,

                )

            )

        for road in roads:

            graph.add_edge(

                Edge(

                    source=road.source,

                    destination=road.destination,

                    distance=road.distance,

                    travel_time=road.travel_time,

                    traffic_factor=road.traffic_factor,

                    road_closed=road.closed,

                    road_name=road.name,

                )

            )

        return graph