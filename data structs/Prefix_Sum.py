def prefix_sum(arr):
    out = [0]*len(arr)
    for i in range(len(arr)):
        out[i] = out[i-1] + arr[i]
    return out