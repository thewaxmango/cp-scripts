from collections.abc import Callable

def _sum(a, b) -> int:
    return a + b

def Segment_Tree(arr: list, func: Callable = _sum) -> list:
    N = len(arr)
    st: list = [0] * (2 * N)
    
    for i in range(N): 
        st[N + i] = arr[i]
    for i in range(N - 1, 0, -1):
        st[i] = func(st[i << 1], st[i << 1 | 1])
    
    return st + [func]
  
def update_segtree(st: list, idx: int, value):
    N = len(st) // 2
    func: Callable = st[-1]
    
    st[idx + N] = value
    idx = idx + N
    i = idx
    while i > 1:
        st[i >> 1] = func(st[i], st[i ^ 1])
        i >>= 1
  
# r NOT INCLUSIVE
def query_segtree(st: list, l: int, r: int):
    N = len(st) // 2
    func: Callable = st[-1]
    
    res = 0
    l += N
    r += N
      
    while l < r :
        if (l & 1):
            res = func(res, st[l])
            l += 1
        if (r & 1):
            r -= 1
            res = func(res, st[r])  
        l >>= 1
        r >>= 1
      
    return res
  
if __name__ == "__main__" : 
    print(_sum(1, 2))
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 
    n = len(a) 
    t = Segment_Tree(a)
    print(query_segtree(t, 1, 3))
    update_segtree(t, 2, 1)
    print(query_segtree(t, 1, 3))