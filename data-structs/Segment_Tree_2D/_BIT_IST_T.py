from Implicit_Segtree_T import SSNodeT
from typing import Optional, TypeVar, Generic, Callable

#^ querying is inclusive
T = TypeVar('T')
class BIT_IST(Generic[T]):
    def __init__(self, operation: Callable[[T, T], T], default: T, size = 2 << 17) -> None:
        self.size = size
        self.op = operation
        self.dft = default
        self.st: list[SSNodeT[T]] = [SSNodeT(operation, default)] * size

    def update(self, x: int, y: int, val: T) -> None:
        while x < self.size:
            self.st[x].update(y, val)
            x += x & -x
    
    def query(self, xl: int, xr: int, yl: int, yr: int) -> T:
        pass
    