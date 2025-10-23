# FROM TITAN-23's LIBRARY

# cartesian tree in-order traversal is same is original data struct
# parent always smaller than children

def Cartesian_Tree(a: list) -> tuple[list, list, list]:
    par = [-1] * len(a)
    left = [-1] * len(a)
    right = [-1] * len(a)
    path = []
    for i, aa in enumerate(a):
        pre = -1
        while path and aa < a[path[-1]]:
            pre = path.pop()
        if pre != -1:
            par[pre] = i
        if path:
            par[i] = path[-1]
        path.append(i)
    for i, p in enumerate(par):
        if p == -1:
            continue
        if i < p:
            left[p] = i
        else:
            right[p] = i
    return par, left, right

arr = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]
ctp, ctl, ctr = Cartesian_Tree(arr)
print(*ctp)