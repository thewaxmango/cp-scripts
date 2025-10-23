from Suffix_Array_LCP import Suffix_Array, LCPrefix

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