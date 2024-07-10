from bisect import bisect_left as bsl, bisect_right as bsr

def Persistent_Array(arr: list, time: int = -1) -> list[list[tuple]]:
    return [[(time, v)] for i, v in enumerate(arr)]

def pa_get_before(PA: list[list[tuple]], idx: int, time: int):
    subidx = bsr(PA[idx], (time, float("inf"))) - 1
    if subidx >= len(PA[idx]):
        return None
    return PA[idx][subidx]

def pa_get_after(PA: list[list[tuple]], idx: int, time: int):
    subidx = bsl(PA[idx], (time, float("-inf")))
    if subidx >= len(PA[idx]):
        return None
    return PA[idx][subidx]

def pa_update(PA: list[list[tuple]], idx: int, value, time: int) -> bool:
    if time <= PA[idx][-1][0]:
        return False
    PA[idx].append((time, value))
    return True