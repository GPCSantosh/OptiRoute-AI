from __future__ import annotations


class DisjointSet:
    """
    Union-Find (Disjoint Set Union)

    Time Complexity:
        make_set : O(1)
        find     : O(α(n))
        union    : O(α(n))

    Space Complexity:
        O(n)

    Uses:
        - Kruskal MST
        - Connected Components
        - Cycle Detection
    """

    def __init__(self) -> None:
        self.parent: dict[str, str] = {}
        self.rank: dict[str, int] = {}

    def make_set(self, node: str) -> None:
        """
        Creates a new independent set.
        """
        self.parent[node] = node
        self.rank[node] = 0

    def find(self, node: str) -> str:
        """
        Finds representative of the set
        using Path Compression.
        """

        if self.parent[node] != node:
            self.parent[node] = self.find(
                self.parent[node]
            )

        return self.parent[node]

    def union(
        self,
        node1: str,
        node2: str,
    ) -> bool:
        """
        Union by Rank.

        Returns
        -------
        True
            if union happened.

        False
            if both nodes already belong
            to the same set.
        """

        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2

        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1

        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True

    def connected(
        self,
        node1: str,
        node2: str,
    ) -> bool:
        """
        Returns whether two nodes belong
        to the same connected component.
        """

        return self.find(node1) == self.find(node2)

    def reset(self) -> None:
        """
        Clears all sets.
        """

        self.parent.clear()
        self.rank.clear()

    def __len__(self) -> int:
        return len(self.parent)

    def __contains__(
        self,
        node: str,
    ) -> bool:
        return node in self.parent

    def __repr__(self) -> str:
        return (
            f"DisjointSet("
            f"sets={len(self.parent)})"
        )