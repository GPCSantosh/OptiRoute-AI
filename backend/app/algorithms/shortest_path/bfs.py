from collections import deque

from app.algorithms.graph.graph import Graph


class BFS:

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

        queue = deque([start])

        order = []

        while queue:

            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            order.append(node)

            for edge in self.graph.neighbors(node):

                if edge.destination not in visited:
                    queue.append(
                        edge.destination
                    )

        return order