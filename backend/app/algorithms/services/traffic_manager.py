class TrafficManager:

    """
    Manages dynamic traffic updates.
    """

    def __init__(self):

        self.traffic = {}

    def update(
        self,
        source,
        destination,
        factor,
    ):

        self.traffic[
            (
                source,
                destination,
            )
        ] = factor

    def get_factor(
        self,
        source,
        destination,
    ):

        return self.traffic.get(
            (
                source,
                destination,
            ),
            1.0,
        )

    def clear(self):

        self.traffic.clear()