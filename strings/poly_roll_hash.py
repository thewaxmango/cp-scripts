_HASH_MOD = 10**9 + 7
_HASH_PRIME = 257

def power_precomp(P = _HASH_PRIME, M = _HASH_MOD, N = 10):
    table = [P]
    for _ in range(N-1):
        table.append(table[-1]**2 % M)
    return table

_HASH_PRIME_TABLE = power_precomp()

def hash(string, P, M):
    sum, coeff = 0, 1
    for c in string:
        sum += ord(c) * coeff
        coeff = coeff * P % M
    return sum

def get_prime_power(power):
    product, i = 1, 0
    while power:
        if power & 1:
            product = product * _HASH_PRIME_TABLE[i] % _HASH_MOD
        power <<= 1
    return product