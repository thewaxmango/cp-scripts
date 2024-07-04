def Suffix_Array(s: str):
    return SAIS([ord(c) for c in s])

def LCPrefix(s: str, SA: list[int]):
    return KASAI([ord(c) for c in s], SA)

def SAIS(A: list[int]):
    n = len(A)
    buckets = [0] * (max(A) + 2)
    for a in A:
        buckets[a + 1] += 1
    for b in range(1, len(buckets)):
        buckets[b] += buckets[b - 1]
    isL = [1] * n
    for i in reversed(range(n - 1)):
        isL[i] = +(A[i] > A[i + 1]) if A[i] != A[i + 1] else isL[i + 1]

    def induced_sort(LMS):
        SA = [-1] * (n)
        SA.append(n)
        endpoint = buckets[1:]
        for j in reversed(LMS):
            endpoint[A[j]] -= 1
            SA[endpoint[A[j]]] = j
        startpoint = buckets[:-1]
        for i in range(-1, n):
            j = SA[i] - 1
            if j >= 0 and isL[j]:
                SA[startpoint[A[j]]] = j
                startpoint[A[j]] += 1
        SA.pop()
        endpoint = buckets[1:]
        for i in reversed(range(n)):
            j = SA[i] - 1
            if j >= 0 and not isL[j]:
                endpoint[A[j]] -= 1
                SA[endpoint[A[j]]] = j
        return SA

    isLMS = [+(i and isL[i - 1] and not isL[i]) for i in range(n)]
    isLMS.append(1)
    LMS = [i for i in range(n) if isLMS[i]]
    if len(LMS) > 1:
        SA = induced_sort(LMS)
        LMS2 = [i for i in SA if isLMS[i]]
        prev = -1
        j = 0
        for i in LMS2:
            i1 = prev
            i2 = i
            while prev >= 0 and A[i1] == A[i2]:
                i1 += 1
                i2 += 1
                if isLMS[i1] or isLMS[i2]:
                    j -= isLMS[i1] and isLMS[i2]
                    break
            j += 1
            prev = i
            SA[i] = j
        LMS = [LMS[i] for i in SAIS([SA[i] for i in LMS])]
    return induced_sort(LMS)

def KASAI(A, SA):
    n = len(A)
    rank = [0] * n
    for i in range(n):
        rank[SA[i]] = i
    LCP = [0] * (n - 1)
    k = 0
    for i in range(n):
        SAind = rank[i]
        if SAind == n - 1:
            continue
        j = SA[SAind + 1]
        while i + k < n and A[i + k] == A[j + k]:
            k += 1
        LCP[SAind] = k
        k -= k > 0
    return LCP

def LCSubstr(S: str, T: str) -> tuple[int, int, int]:
    n = len(S)
    m = len(T)
    R = S + "$" + T
    SA = Suffix_Array(R)
    LCP = LCPrefix(R, SA)
    N = n + m + 1

    m = 0
    vs = [[] for _ in range(N)]
    for i in range(N - 1):
        vs[LCP[i]].append(i)
        if LCP[i] > m and (SA[i] < n) ^ (SA[i + 1] < n):
            m = LCP[i]

    if m <= 0:
        return (0, 0, 0)
    for i in vs[m]:
        if (SA[i] < n) != (SA[i + 1] < n):
            if SA[i] < n:
                return (SA[i], SA[i + 1] - n - 1, m)
            else:
                return (SA[i + 1], SA[i] - n - 1, m)
    return (0, 0, 0)

s, t = input(), input()
a, b, l = LCSubstr(s, t)
print(a, a+l, b, b+l)