from bisect import bisect_left as bsl, bisect_right as bsr
from collections.abc import Callable
from typing import Union
Numeric = Union[int, float]

from Persistent_Array import *

def _sum(a, b) -> int:
    return a + b

def Persistent_Segment_Tree(arr: list, time: Numeric = -1, func: Callable = _sum) -> list:
    N = len(arr)
    pst: list[list[tuple]] = [[] for _ in range(2*N)]
    
    for i in range(N): 
        pst[N + i].append((time, arr[i]))
    for i in range(N - 1, 0, -1):
        pst[i].append((time, func(pst[i << 1][0][1], pst[i << 1 | 1][0][1])))
    
    return pst + [time, func]

def update_PST(pst: list, idx: int, value, time: Numeric) -> bool:
    N = len(pst) // 2 - 1
    func: Callable = pst[-1]
    max_time = pst[-2]
    
    if max_time > time or pst[idx + N][-1][0] >= time:
        return False
    pst[idx + N].append((time, value))
    
    idx = idx + N
    i = idx
    while i > 1:
        if pst[i >> 1][-1][0] == time:
            pst[i >> 1][-1].pop()
        pst[i >> 1].append((max(pst[i][-1][0], pst[i ^ 1][-1][0]), func(pst[i][-1][1], pst[i ^ 1][-1][1])))
        i >>= 1
        
    return True

def query_PST_before(pst: list, l: int, r: int, time: Numeric):
    pass

def query_PST_after(pst: list, l: int, r: int, time: Numeric):
    pass