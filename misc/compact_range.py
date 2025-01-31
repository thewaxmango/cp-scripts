def compact(arr: list):
    res = arr
    keyarr = sorted((v, i) for i, v in enumerate(arr))
    k = 0
    for i in range(1, len(arr)):
        if keyarr[i][0] != keyarr[i-1][0]:
            k += 1
        res[keyarr[i][1]] = k
    return res