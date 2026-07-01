from app.algorithms.graph.graph import Graph


class DFS:

    def __init__(
        self,
        graph: Graph,
    ):
        self.graph = graph

    def traverse(
        self,
        start: str,
    ) -> list[str]:

        visited = set()

        order = []

        self._dfs(
            start,
            visited,
            order,
        )

        return order

    def _dfs(
        self,
        node: str,
        visited: set,
        order: list,
    ):

        visited.add(node)

        order.append(node)

        for edge in self.graph.neighbors(node):

            if edge.destination not in visited:

                self._dfs(
                    edge.destination,
                    visited,
                    order,
                )