def phi(n: int) -> int:
    return 0

# array of phi from 1 to n
def phis(n: int) -> list[int]:
    res, sieve = [1]*(n+1), [-1]*(n+1) 
    for i in range(2, n+1):
        if sieve[i] == -1:
            sieve[i] = i
            sieve[i*i::i] = [i] * ((n-i*i)//i+1)
    for i in range(2, n+1):
        p, j = sieve[i], i
        while j % p == 0 and p != -1:
            res[i] *= p
            j //= p
        res[i] = res[i] // p * (p-1) * res[j]
    return res

print(phis(10))