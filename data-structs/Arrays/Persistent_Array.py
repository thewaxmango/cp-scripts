from bisect import bisect_left as bsl, bisect_right as bsr
from typing import Union
Numeric = Union[int, float]

def Persistent_Array(arr: list, time: Numeric = -1) -> list[list[tuple]]:
    return [[(time, v)] for v in arr]

# time inclusive
def pa_get_before(PA: list[list[tuple]], idx: int, time: Numeric):
    subidx = bsr(PA[idx], (time, float("inf"))) - 1
    if subidx < 0:
        return None
    return PA[idx][subidx]

# time inclusive
def pa_get_after(PA: list[list[tuple]], idx: int, time: Numeric):
    subidx = bsl(PA[idx], (time, float("-inf")))
    if subidx >= len(PA[idx]):
        return None
    return PA[idx][subidx]

def pa_update(PA: list[list[tuple]], idx: int, value, time: Numeric) -> bool:
    if time <= PA[idx][-1][0]:
        return False
    PA[idx].append((time, value))
    return True