from app.algorithms.graph.graph import Graph
from app.algorithms.graph.priority_queue import PriorityQueue


class Prim:

    """
    Time Complexity:
        O(E log V)
    """

    def __init__(
        self,
        graph: Graph,
    ):

        self.graph = graph

    def minimum_spanning_tree(
        self,
        start: str,
    ):

        visited = set()

        pq = PriorityQueue()

        mst = []

        total_weight = 0

        visited.add(start)

        for edge in self.graph.neighbors(start):

            pq.push(
                edge.distance,
                edge,
            )

        while not pq.empty():

            weight, edge = pq.pop()

            if edge.destination in visited:
                continue

            visited.add(edge.destination)

            mst.append(edge)

            total_weight += weight

            for next_edge in self.graph.neighbors(
                edge.destination
            ):

                if (
                    next_edge.destination
                    not in visited
                ):

                    pq.push(
                        next_edge.distance,
                        next_edge,
                    )

        return {

            "algorithm": "Prim",

            "edges": mst,

            "total_weight": total_weight,

        }