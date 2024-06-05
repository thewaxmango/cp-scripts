def precomp():
    global PRIMES, PRECOMP_BIN, PRECOMP_BIN_2
    # importing primes
    PRIMES = []
    MOD = 10**9 + 9
    with open("primes.txt", "r") as plist:
        for p in plist:
            PRIMES.append(int(p))
    # precomputing power-of-2 powers of 1e9+7
    PRECOMP_BIN = [1]
    PRECOMP_BIN_2 = [1]
    for k in range(30):
        PRECOMP_BIN.append(PRECOMP_BIN[-1] * PRIMES[0] % MOD)
        PRECOMP_BIN_2.append(PRECOMP_BIN_2[-1] * PRIMES[1] % MOD)

def poly_roll_hash(string : str, encoding_prime : int = 0):
    assert 0 <= encoding_prime < 200, "encoding_prime invalid"
    
