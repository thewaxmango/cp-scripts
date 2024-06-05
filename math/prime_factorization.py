from math import gcd

def primes_to(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def f(x, n):
    return (x**2 + 1)%n

def pollard(n):
    x, y, d = 2, 2, 1
    
    while d == 1:
        x, y = f(x, n), f(f(y, n), n)
        d = gcd(abs(x - y), n)
        
    return d


stack = [897612484786617600]
primes = primes_to(10**6)
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

print(factors)
print(pollard(323))
print(pollard(17575))
    