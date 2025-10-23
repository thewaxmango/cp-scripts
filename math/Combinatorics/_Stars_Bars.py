# --------- CHOOSE_FACTORIAL.PY ------------
MOD = 10**9 + 7
def factorials(limit=4*10**5 + 10):
    fact, invfact = [1], [1]
    for v in range(1, limit):
        fact.append(fact[-1] * v % MOD)
        invfact.append(pow(fact[-1], MOD - 2, MOD))
    return fact, invfact
fact, invfact = factorials()
def choose(n, x):
    return fact[n] * invfact[x] % MOD * invfact[n - x] % MOD
# -----------------------------------------

# n items, k nonempty buckets
def stars_bars1(n:int, k:int) -> int:
    return choose(n-1, k-1)

# n items, k buckets
def stars_bars_2(n:int, k:int) -> int:
    return choose(n+k-1, k-1)