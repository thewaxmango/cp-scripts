from math import gcd

def pollard(n):
    def f(x, n):
        return (x**2 + 1)%n
    x, y, d = 2, 2, 1
    while d == 1:
        x, y = f(x, n), f(f(y, n), n)
        d = gcd(abs(x - y), n)
    return d

def pollard2(n):
    def f(x): return (x**2 + 1) % n
    x, y, t, prd, i = 0, 0, 30, 2, 1
    while t % 40 or gcd(prd, n) == 1:
        t += 1
        if x == y: 
            i += 1
            x, y = i, f(x)
        q = prd * (max(x, y) - min(x, y)) % n
        if q:
            prd = q
        x, y = f(x), f(f(y))
    return gcd(prd, n)

def factor(n):
    stack = [n]
    factors = {}
    while stack:
        n = stack.pop()
        wn = pollard(n)
        if n == wn:
            if wn not in factors:
                factors[wn] = 0
            factors[wn] += 1
        else:
            stack.append(wn)
            stack.append(n//wn)
    return factors

print(factor(897612484786617600))
print(factor(24))
print(pollard(323))
print(pollard(17575))
    