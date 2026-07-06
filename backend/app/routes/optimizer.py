from app.algorithms.shortest_path.astar import AStar
from app.algorithms.shortest_path.dijkstra import Dijkstra


class RouteOptimizer:
    """
    Route Optimizer

    Supported Algorithms
    --------------------
    - dijkstra
    - astar
    - a*

    This class validates inputs and dispatches
    the request to the selected shortest-path algorithm.
    """

    def __init__(self, graph):
        self.graph = graph

    def solve(
        self,
        source: str,
        destination: str,
        algorithm: str,
    ):

        # -----------------------------
        # Normalize Input
        # -----------------------------

        source = (source or "").strip()
        destination = (destination or "").strip()
        algorithm = (algorithm or "").strip().lower()

        # -----------------------------
        # Validate Input
        # -----------------------------

        if source == "":
            return {
                "success": False,
                "message": "Source cannot be empty."
            }

        if destination == "":
            return {
                "success": False,
                "message": "Destination cannot be empty."
            }

        if algorithm not in (
            "dijkstra",
            "astar",
            "a*",
        ):
            return {
                "success": False,
                "message": (
                    f"Unsupported algorithm '{algorithm}'. "
                    "Supported algorithms: dijkstra, astar."
                ),
            }

        # -----------------------------
        # Run Algorithm
        # -----------------------------

        if algorithm == "dijkstra":

            solver = Dijkstra(self.graph)

            result = solver.shortest_path(
                source,
                destination,
            )

        else:

            solver = AStar(self.graph)

            result = solver.shortest_path(
                source,
                destination,
            )

        # -----------------------------
        # Standardize Response
        # -----------------------------

        if result.get("path"):

            result["success"] = True

        else:

            result["success"] = False

            result["distance"] = 0

            result["path"] = []

            result.setdefault(
                "visited_nodes",
                0,
            )

            result.setdefault(
                "expanded_nodes",
                0,
            )

            result.setdefault(
                "execution_time_ms",
                0,
            )

            result.setdefault(
                "message",
                "No route found.",
            )

        return result