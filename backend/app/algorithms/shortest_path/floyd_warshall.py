from math import inf

from app.algorithms.graph.graph import Graph


class FloydWarshall:

    """
    Time Complexity:
        O(V³)

    Space Complexity:
        O(V²)
    """

    def __init__(
        self,
        graph: Graph,
    ):

        self.graph = graph

    def compute(self):

        vertices = self.graph.vertices()

        n = len(vertices)

        index = {

            vertex: i

            for i, vertex in enumerate(vertices)

        }

        distance = [

            [inf] * n

            for _ in range(n)

        ]

        for i in range(n):
            distance[i][i] = 0

        for edge in self.graph.edges():

            i = index[edge.source]

            j = index[edge.destination]

            distance[i][j] = edge.distance

        for k in range(n):

            for i in range(n):

                for j in range(n):

                    distance[i][j] = min(

                        distance[i][j],

                        distance[i][k]
                        + distance[k][j],

                    )

        return {

            "algorithm": "Floyd Warshall",

            "vertices": vertices,

            "distance_matrix": distance,

        }