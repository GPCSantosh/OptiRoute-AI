import tracemalloc


class MemoryProfiler:

    def __enter__(self):

        tracemalloc.start()

        return self

    def __exit__(

        self,

        exc_type,

        exc,

        tb,

    ):

        self.current, self.peak = (
            tracemalloc.get_traced_memory()
        )

        tracemalloc.stop()