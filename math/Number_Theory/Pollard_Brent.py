from math import sqrt, floor

def naive_factor(x: int) -> list[int]:
    res = []
    for i in range(2, floor(sqrt(x))+1):
        while x % i == 0:
            res.append(i)
            x //= i
    if x != 1:
        res.append(x)
    return res

# https://judge.yosupo.jp/submission/6175
"""
https://twitter.com/kiri8128/status/1240504897419673600
https://twitter.com/kiri8128/status/1241033090773860353
"""

from collections import defaultdict
from functools import lru_cache
from math import gcd
from typing import Dict, Optional


@lru_cache(maxsize=None)
def is_prime_miller_rabin(n: int) -> bool:
    """Miller–Rabin primality test"""
    if n < 2:
        return False
    elif n in {2, 3, 5, 7, 11, 61}:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
        return False

    if n < (1 << 32):
        L = [2, 7, 61]
    elif n < (1 << 48):
        L = [2, 3, 5, 7, 11, 13, 17]
    else:
        L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    d = n - 1
    d = d // (d & -d)

    for a in L:
        y = pow(a, d, n)
        if y == 1:
            continue
        t = d
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1:
                return False
            t <<= 1
    return True

def find_factor_rho(n: int) -> Optional[int]:
    if n < 2:
        return None
    m = 1 << n.bit_length() // 8 + 1

    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if is_prime_miller_rabin(g):
                return g
            elif is_prime_miller_rabin(n // g):
                return n // g
    return None

def factor(n: int) -> Dict[int, int]:
    prime_factors = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            prime_factors[i] += 1
        i += 1 + i % 2
        if i != 101 or n < 1 << 20:
            continue
        while n > 1:
            if is_prime_miller_rabin(n):
                prime_factors[n], n = 1, 1
                break
            j = find_factor_rho(n)
            while n % j == 0:
                n //= j
                prime_factors[j] += 1
    if n > 1:
        prime_factors[n] += 1
    return prime_factors  # the keys are unsorted

print(factor(999381247093216751))