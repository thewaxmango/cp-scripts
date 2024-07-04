# Longest Common Subsequence

def LCSubseq_DP(x: str, y: str) -> list[list[int]]:
    m: int = len(x)
    n: int = len(y)
    dp: list[list[int]] = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp

def LCSubseq(x: str, y: str) -> int:
    dp = LCSubseq_DP(x, y)
    return dp[-1][-1]

def LCSubseq_Str(x: str, y: str) -> str:
    dp = LCSubseq_DP(x, y)

    res = []
    a, b = len(x), len(y)
    while a != 0 and b != 0:
        if dp[a][b] == dp[a - 1][b]:
            a -= 1
        elif dp[a][b] == dp[a][b - 1]:
            b -= 1
        else:
            res.append(x[a - 1])
            a -= 1
            b -= 1

    return "".join(res[::-1])

if __name__ == "__main__":
    print(*LCSubseq_DP("abcb", "acb"), sep="\n")