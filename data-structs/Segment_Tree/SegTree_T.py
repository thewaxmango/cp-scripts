from typing import Callable, TypeVar, Generic

T = TypeVar('T')  # Define type variable "T"
class SegTree(Generic[T]):
    def __init__(self, array: list[T], default: T, func: Callable[[T, T], T]) -> None:
        self.n: int = len(array)
        self.T_def = default
        self.st: list[T] = [default for _ in range(2 * self.n)]
        self.func = func
        
        self.build(array)
    
    def __getitem__(self, index: int) -> T:
        return self.st[self.n + index % self.n]
    
    def __setitem__(self, index: int, value: T) -> None:
        self.update(index, value)
    
    def build(self, array: list[T]) -> None:
        self.st[self.n:] = array
        for i in range(self.n - 1, 0, -1):
            self.st[i] = self.func(self.st[i << 1], self.st[i << 1 | 1])
    
    def update(self, index: int, value: T) -> None:
        index += self.n
        self.st[index] = value
        while index > 1:
            self.st[index >> 1] = self.func(self.st[index], self.st[index ^ 1])
            index >>= 1
    
    # r not inclusive
    def query(self, l: int, r: int) -> T:
        res: T = self.T_def
        l += self.n
        r += self.n
        while l < r:
            if (l & 1):
                res = self.func(res, self.st[l])
                l += 1
            if (r & 1):
                r -= 1
                res = self.func(res, self.st[r])  
            l >>= 1
            r >>= 1
        return res