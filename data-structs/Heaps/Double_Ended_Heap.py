# Taken from https://judge.yosupo.jp/submission/216060

from heapq import heapify, heappush, heappop

class Double_Ended_Heap:

    def __init__(self, data) -> None:
        self.min_heap = data
        self.max_heap = [-i for i in data]
        self.removed_min = []
        self.removed_max = []
        heapify(self.min_heap)
        heapify(self.max_heap)

    def add(self, val) -> None:
        heappush(self.min_heap, val)
        heappush(self.max_heap, -val)

    def discard(self, val) -> None:
        heappush(self.removed_min, val)
        heappush(self.removed_max, -val)

    def _remove_duplicates(self, heap, removed_heap) -> None:
        while heap and removed_heap and heap[0] == removed_heap[0]:
            heappop(heap)
            heappop(removed_heap)

    def pop_max(self):
        self._remove_duplicates(self.max_heap, self.removed_max)
        # if not self.max_heap:
        #     raise IndexError("pop from an empty heap")
        max_value = -heappop(self.max_heap)
        heappush(self.removed_min, max_value)
        return max_value

    def pop_min(self):
        self._remove_duplicates(self.min_heap, self.removed_min)
        # if not self.min_heap:
        #     raise IndexError("pop from an empty heap")
        min_value = heappop(self.min_heap)
        heappush(self.removed_max, -min_value)
        return min_value

    def get_max(self):
        self._remove_duplicates(self.max_heap, self.removed_max)
        # if not self.max_heap:
        #     raise IndexError("max value of an empty heap")
        return -self.max_heap[0]

    def get_min(self):
        self._remove_duplicates(self.min_heap, self.removed_min)
        # if not self.min_heap:
        #     raise IndexError("min value of an empty heap")
        return self.min_heap[0]