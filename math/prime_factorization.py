from math import gcd

def pollard(n):
    def f(x, n):
        return (x**2 + 1)%n
    x, y, d = 2, 2, 1
    while d == 1:
        x, y = f(x, n), f(f(y, n), n)
        d = gcd(abs(x - y), n)
    return d

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

print(factor(897612484786617600))
print(pollard(323))
print(pollard(17575))
    