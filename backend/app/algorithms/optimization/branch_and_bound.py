from __future__ import annotations

from math import inf

from app.algorithms.graph.graph import Graph


class BranchAndBound:
    """
    Exact TSP using Branch and Bound.

    Suitable for small graphs.
    """

    def __init__(
        self,
        graph: Graph,
    ):
        self.graph = graph

        self.best_cost = inf

        self.best_path = []

    def solve(
        self,
        start: str,
    ):

        self._dfs(
            current=start,
            start=start,
            visited={start},
            path=[start],
            cost=0,
        )

        return {

            "algorithm": "Branch and Bound",

            "route": self.best_path,

            "distance": self.best_cost,
        }

    def _dfs(
        self,
        current,
        start,
        visited,
        path,
        cost,
    ):

        if len(visited) == len(self.graph):

            for edge in self.graph.neighbors(current):

                if edge.destination == start:

                    total = cost + edge.distance

                    if total < self.best_cost:

                        self.best_cost = total

                        self.best_path = path + [start]

                    return

        if cost >= self.best_cost:
            return

        for edge in self.graph.neighbors(current):

            if edge.destination in visited:
                continue

            visited.add(edge.destination)

            self._dfs(
                edge.destination,
                start,
                visited,
                path + [edge.destination],
                cost + edge.distance,
            )

            visited.remove(edge.destination)