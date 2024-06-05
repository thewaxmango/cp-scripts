import math

MOD = 10**9 + 7

fact = [1]
invfact = [1]
for v in range(1, 2*10**5 + 1):
    fact.append(fact[-1] * v % MOD)
    invfact.append(pow(fact[-1], MOD - 2, MOD))

def choose(n, x):
    return fact[n] * invfact[x] % MOD * invfact[n - x] % MOD

print(math.gcd(10, 5))