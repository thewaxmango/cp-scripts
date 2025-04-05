from typing import Callable, TypeVar, Generic
T = TypeVar('T')
class SegTree(Generic[T]):
    def __init__(self, n: int, unit: T, f: Callable[[T, T], T]) -> None:
        self.n = n
        self.unit = unit
        self.st = [unit for _ in range(2 * self.n)]
        self.f = f
    def update(self, idx: int, val: T) -> None:
        idx += self.n
        self.st[idx] = val
        while (idx := idx // 2):
            self.st[idx] = self.f(self.st[idx*2], self.st[idx*2+1])
    def query(self, l: int, r: int) -> T: # right-exclusive
        ra, rb = self.unit, self.unit
        l, r = l + self.n, r + self.n 
        while l < r:
            if l % 2: 
                ra = self.f(ra, self.st[l])
                l += 1
            if r % 2:
                r -= 1
                rb = self.f(self.st[r], rb)
            l, r = l // 2, r // 2
        return self.f(ra, rb)