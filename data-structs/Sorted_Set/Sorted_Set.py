# Taken from https://judge.yosupo.jp/submission/259470

import math
from bisect import bisect_left, bisect_right

class SortedSet:
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    __slots__ = ("buckets", "size")

    def __init__(self, iterable=[]) -> None:
        """Create a new SortedSet from an iterable. O(N log N)."""
        sorted_unique_elements = sorted(set(iterable))
        self.size = len(sorted_unique_elements)
        self._build_buckets(sorted_unique_elements)

    def _build_buckets(self, sorted_elements: list) -> None:
        """Build the buckets from a sorted list of elements."""
        n = self.size
        num_buckets = math.ceil(math.sqrt(n / self.BUCKET_RATIO))
        self.buckets = [
            sorted_elements[n * i // num_buckets : n * (i + 1) // num_buckets]
            for i in range(num_buckets)
        ]

    def __iter__(self):
        for bucket in self.buckets:
            yield from bucket

    def __reversed__(self):
        for bucket in reversed(self.buckets):
            yield from reversed(bucket)

    def __eq__(self, other) -> bool:
        if isinstance(other, SortedSet):
            return list(self) == list(other)
        return False

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({set(self)})"

    __repr__ = __str__

    def _find_bucket(self, x) -> tuple[list, int, int]:
        """Find the appropriate bucket and the index within that bucket for x."""
        for i, bucket in enumerate(self.buckets):
            if x <= bucket[-1]:
                break
        return (bucket, i, bisect_left(bucket, x))

    def __contains__(self, x) -> bool:
        if self.size == 0:
            return False
        bucket, _, i = self._find_bucket(x)
        return i != len(bucket) and bucket[i] == x

    def add(self, x) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.buckets = [[x]]
            self.size = 1
            return True

        bucket, bi, i = self._find_bucket(x)
        if i < len(bucket) and bucket[i] == x:
            return False

        bucket.insert(i, x)
        self.size += 1
        if len(bucket) > len(self.buckets) * self.SPLIT_RATIO:
            mid = len(bucket) >> 1
            self.buckets[bi : bi + 1] = [bucket[:mid], bucket[mid:]]
        return True

    def discard(self, x) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        bucket, bi, i = self._find_bucket(x)
        if i == len(bucket) or bucket[i] != x:
            return False
        self._pop(bucket, bi, i)
        return True

    def _pop(self, bucket: list, bi: int, i: int):
        res = bucket.pop(i)
        self.size -= 1
        if not bucket:
            del self.buckets[bi]
        return res


    def le(self, x):
        "Find the largest element <= x, or None if it doesn't exist."
        for bucket in reversed(self.buckets):
            if bucket[0] <= x:
                return bucket[bisect_right(bucket, x) - 1]
        return -1

    def ge(self, x):
        "Find the smallest element >= x, or None if it doesn't exist."
        for bucket in self.buckets:
            if bucket[-1] >= x:
                return bucket[bisect_left(bucket, x)]
        return -1

    def __getitem__(self, i: int):
        """Return the element at index i."""
        if i < 0:
            i += self.size
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range")

        for bucket in self.buckets:
            if i < len(bucket):
                return bucket[i]
            i -= len(bucket)

    def pop(self, i: int = -1):
        "Pop and return the i-th element."
        if i < 0:
            i += self.size
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range")

        for bucket_idx, bucket in enumerate(self.buckets):
            if i < len(bucket):
                return self._pop(bucket, bucket_idx, i)
            i -= len(bucket)

    def index(self, x) -> int:
        "Count the number of elements < x."
        cnt = 0
        for bucket in self.buckets:
            if bucket[-1] >= x:
                return cnt + bisect_left(bucket, x)
            cnt += len(bucket)
        return cnt

    def index_right(self, x) -> int:
        "Count the number of elements <= x."
        cnt = 0
        for bucket in self.buckets:
            if bucket[-1] > x:
                return cnt + bisect_right(bucket, x)
            cnt += len(bucket)
        return cnt