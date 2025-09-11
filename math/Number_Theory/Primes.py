def primes_to(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def linear_sieve(n):
    lp = [0]*(n+1)
    pr = []
    for i in range(2, n+1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        j = 0
        while i * pr[j] <= n:
            lp[i * pr[j]] = pr[j]
            if pr[j] == lp[i]:
                break
            j += 1
    return lp, pr
