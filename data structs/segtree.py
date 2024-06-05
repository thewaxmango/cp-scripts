segtreeN = 2**17

def build(arr):
    tree = [0] * (2 * segtreeN)
    for i in range(n): 
        tree[segtreeN + i] = arr[i]
    for i in range(segtreeN - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
    return tree
  
def updateTreeNode(tree, p, value): 
    tree[p + segtreeN] = value
    p = p + segtreeN
    i = p
    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1
  
# r is not inclusive
def query(tree, l, r): 
    res = 0; 
    l += segtreeN
    r += segtreeN
      
    while l < r :
        if (l & 1):
            res += tree[l] 
            l += 1
        if (r & 1):
            r -= 1
            res += tree[r]  
        l >>= 1
        r >>= 1
      
    return res
  
if __name__ == "__main__" : 
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 
    n = len(a) 
    build(a)
    print(query(1, 3))
    updateTreeNode(2, 1)
    print(query(1, 3))