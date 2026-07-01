from __future__ import annotations

from typing import Any


class PriorityQueue:
    """
    Custom Min Priority Queue.

    Uses a binary min-heap with an insertion counter to
    avoid comparing objects having the same priority.

    Time Complexity
    ----------------
    Push : O(log n)

    Pop  : O(log n)

    Peek : O(1)
    """

    def __init__(self):

        self.heap: list[tuple[float, int, Any]] = []

        self.counter = 0

    # --------------------------------------------------

    def empty(self) -> bool:

        return len(self.heap) == 0

    # --------------------------------------------------

    def size(self) -> int:

        return len(self.heap)

    # --------------------------------------------------

    def push(
        self,
        priority: float,
        value: Any,
    ) -> None:

        self.counter += 1

        self.heap.append(
            (
                priority,
                self.counter,
                value,
            )
        )

        self._heapify_up()

    # --------------------------------------------------

    def pop(self):

        if self.empty():
            return None

        self.heap[0], self.heap[-1] = (
            self.heap[-1],
            self.heap[0],
        )

        priority, _, value = self.heap.pop()

        if self.heap:
            self._heapify_down()

        return priority, value

    # --------------------------------------------------

    def peek(self):

        if self.empty():
            return None

        priority, _, value = self.heap[0]

        return priority, value

    # --------------------------------------------------

    def clear(self):

        self.heap.clear()

        self.counter = 0

    # --------------------------------------------------

    def _heapify_up(self):

        index = len(self.heap) - 1

        while index > 0:

            parent = (index - 1) // 2

            if self.heap[parent][:2] <= self.heap[index][:2]:
                break

            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent],
            )

            index = parent

    # --------------------------------------------------

    def _heapify_down(self):

        index = 0

        length = len(self.heap)

        while True:

            left = 2 * index + 1

            right = 2 * index + 2

            smallest = index

            if (
                left < length
                and self.heap[left][:2]
                < self.heap[smallest][:2]
            ):
                smallest = left

            if (
                right < length
                and self.heap[right][:2]
                < self.heap[smallest][:2]
            ):
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )

            index = smallest

    # --------------------------------------------------

    def __len__(self):

        return len(self.heap)

    # --------------------------------------------------

    def __bool__(self):

        return not self.empty()

    # --------------------------------------------------

    def __repr__(self):

        return (
            f"PriorityQueue(size={len(self.heap)})"
        )