def inversions_merge(arr: list) -> tuple[int, list]:
    n = len(arr)
    if n < 2:
        return (0, arr)
    il, al = inversions_merge(arr[:n//2])
    ir, ar = inversions_merge(arr[n//2:])
    r, a = il + ir, [None]*n
    pl, pr = 0, 0
    ll, lr = len(al), len(ar)
    for i in range(n):
        if pl == ll:
            a[i:] = ar[pr:]
            break
        if pr == lr:
            a[i:] = al[pl:]
            break
        if al[pl] <= ar[pr]:
            a[i] = al[pl]
            pl += 1
        else:
            r += ll - pl
            a[i] = ar[pr]
            pr += 1
    return (r, a)

print(inversions_merge([1, 3, 4, 2]))