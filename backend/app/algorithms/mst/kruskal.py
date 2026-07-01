from app.algorithms.graph.disjoint_set import DisjointSet
from app.algorithms.graph.graph import Graph


class Kruskal:

    """
    Time Complexity:
        O(E log E)
    """

    def __init__(
        self,
        graph: Graph,
    ):

        self.graph = graph

    def minimum_spanning_tree(self):

        ds = DisjointSet()

        for vertex in self.graph.vertices():

            ds.make_set(vertex)

        edges = sorted(

            self.graph.edges(),

            key=lambda edge: edge.distance,

        )

        mst = []

        total_weight = 0

        for edge in edges:

            if ds.union(
                edge.source,
                edge.destination,
            ):

                mst.append(edge)

                total_weight += edge.distance

        return {

            "algorithm": "Kruskal",

            "edges": mst,

            "total_weight": total_weight,

        }