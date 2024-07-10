from collections.abc import Callable

def _sum(a, b) -> int:
    return a + b

def Segment_Tree(arr: list, func: Callable = _sum) -> list:
    N = len(arr)
    tree = [0] * (2*N)
    
    for i in range(n): 
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = func(tree[i << 1], tree[i << 1 | 1])
    
    return tree + [func]
  
def update_Segtree(tree: list, idx: int, value):
    N = len(tree) // 2
    func: Callable = tree[-1]
    
    tree[idx + N] = value
    idx = idx + N
    i = idx
    while i > 1:
        tree[i >> 1] = func(tree[i], tree[i ^ 1])
        i >>= 1
  
# r NOT INCLUSIVE
def Query_Segtree(tree: list, l: int, r: int):
    N = len(tree) // 2
    func: Callable = tree[-1]
    
    res = 0
    l += N
    r += N
      
    while l < r :
        if (l & 1):
            res = func(res, tree[l])
            l += 1
        if (r & 1):
            r -= 1
            res = func(res, tree[r])  
        l >>= 1
        r >>= 1
      
    return res
  
if __name__ == "__main__" : 
    print(_sum(1, 2))
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 
    n = len(a) 
    t = Segment_Tree(a)
    print(Query_Segtree(t, 1, 3))
    update_Segtree(t, 2, 1)
    print(Query_Segtree(t, 1, 3))