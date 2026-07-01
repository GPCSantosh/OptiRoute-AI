from __future__ import annotations


class TwoOpt:
    """
    2-OPT Route Improvement

    Improves an existing TSP route by
    removing edge crossings.

    Complexity
    ----------
    Time:
        O(n²)

    Space:
        O(1)
    """

    @staticmethod
    def optimize(
        route: list[str],
        distance_matrix: dict[tuple[str, str], float],
    ) -> list[str]:

        if len(route) < 4:
            return route

        improved = True

        best = route[:]

        while improved:

            improved = False

            for i in range(1, len(best) - 2):

                for j in range(i + 1, len(best) - 1):

                    new_route = (
                        best[:i]
                        + best[i:j + 1][::-1]
                        + best[j + 1:]
                    )

                    if (
                        TwoOpt.route_cost(
                            new_route,
                            distance_matrix,
                        )
                        <
                        TwoOpt.route_cost(
                            best,
                            distance_matrix,
                        )
                    ):

                        best = new_route

                        improved = True

        return best

    @staticmethod
    def route_cost(
        route,
        distance_matrix,
    ):

        total = 0

        for i in range(
            len(route) - 1
        ):

            total += distance_matrix[
                (
                    route[i],
                    route[i + 1],
                )
            ]

        return total