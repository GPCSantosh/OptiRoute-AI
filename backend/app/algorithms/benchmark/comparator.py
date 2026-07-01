from app.algorithms.shortest_path.astar import AStar
from app.algorithms.shortest_path.dijkstra import Dijkstra

from .memory import MemoryProfiler
from .timer import Timer


class AlgorithmComparator:

    def __init__(

        self,

        graph,

    ):

        self.graph = graph

    def compare(

        self,

        source,

        destination,

    ):

        results = []

        for algorithm in (

            Dijkstra(self.graph),

            AStar(self.graph),

        ):

            with Timer() as timer:

                with MemoryProfiler():

                    result = algorithm.shortest_path(

                        source,

                        destination,

                    )

            result[
                "execution_time_ms"
            ] = round(

                timer.elapsed,

                3,

            )

            results.append(result)

        return results