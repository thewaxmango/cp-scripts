from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, TypeVar, Optional, Generic

T = TypeVar('T')

@dataclass(slots=True)
class IST_Node(Generic[T]):
    l: int
    r: int
    v: T
    nl: Optional[IST_Node] = None
    nr: Optional[IST_Node] = None
    
class IST(Generic[T]):
    def __init__(self, n: int, unit: T, f: Callable[[T, T], T]) -> None:
        self.n = n
        self.unit = unit
        self.f = f
        self.root = IST_Node(0, n-1, unit)
    
    def __upd(self, idx: int, val: T, node: IST_Node) -> None:
        if node.l == node.r == idx:
            node.v = val
            return
        
        m = (node.l + node.r) // 2
        if idx <= m:
            if node.nl == None:
                node.nl = IST_Node(node.l, m, self.unit)
            self.__upd(idx, val, node.nl)
        else:
            if node.nr == None:
                node.nr = IST_Node(m+1, node.r, self.unit)
            self.__upd(idx, val, node.nr)
        
        lv = node.nl.v if node.nl != None else self.unit
        rv = node.nr.v if node.nr != None else self.unit
        node.v = self.f(lv, rv)
    
    def update(self, idx: int, val: T) -> None:
        self.__upd(idx, val, self.root)
        
    def __qu(self, l: int, r: int, node: Optional[IST_Node]) -> T:
        if node == None or l > node.r or r < node.l: 
            return self.unit
        if l <= node.l and r >= node.r: 
            return node.v
        return self.f(self.__qu(l, r, node.nl), self.__qu(l, r, node.nr))
        
    def query(self, l: int, r: int) -> Optional[T]: # not inclusive
        if l >= r: return None
        return self.__qu(l, r-1, self.root) 
    
# Tested for correctness on: https://judge.yosupo.jp/problem/staticrmq
# Results: https://judge.yosupo.jp/submission/279156
# Was not able to use `slots=True` due to python version
def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    ist = IST(n, 10**9, min)
    for i, v in enumerate(a):
        ist.update(i, v)
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(ist.query(l, r))

if __name__ == "__main__":
    main()