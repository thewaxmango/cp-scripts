# translated from CP ALGORITHMS

# enumerates all occurrences of pattern s in text t in O(|t| + |s|) using hash
def Rabin_Karp(s: str, t: str) -> list[int]:
    P, MOD = 31, 10**9 + 7
    S, T = len(s), len(t)
    
    ppow = [1]
    for _ in range(max(S, T)):
        ppow.append(ppow[-1] * P % MOD)
    
    h = [0] * (T+1)
    for i in range(T):
        h[i+1] = (h[i] + ppow[i] * (ord(t[i]) - ord('a') + 1)) % MOD
    h_s = 0
    for i in range(S):
        h_s = (h_s + ppow[i] * (ord(t[i]) - ord('a') + 1)) % MOD
        
    occ = []
    for i in range(0, T - S + 1):
        cur_h = (h[i+S] + MOD - h[i]) % MOD
        if cur_h == h_s * ppow[i] % MOD:
            occ.append(i)
    
    return occ

print(Rabin_Karp("ab", "abbbababaaabaabbaaba"))