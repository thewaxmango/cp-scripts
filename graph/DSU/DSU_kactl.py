# source: kactl

class DSU:
    def __init__(self, size: int) -> None:
        self.e: list[int] = [-1]*size
    def size(self, x: int) -> int:
        return -self.e[self.find(x)]
    def find(self, x: int) -> int:
        return x if self.e[x] < 0 else self.find(self.e[x])
    def join(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.e[a] > self.e[b]: a, b = b, a
        self.e[a] += self.e[b] 
        self.e[b] = a
        return True
    def conn(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)