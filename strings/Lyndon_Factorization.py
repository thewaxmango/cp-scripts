# Translated from CP ALGO

# Separates a string s into substrings s = w_0 + w_1... w_n-1
# where substrings w_i are simple.
# Simple substrings are the lexicographically smallest of all their cyclic rotations
def Duval_Lyndon_Factorization(s: str) -> list[int]:
    N: int = len(s)
    i: int = 0
    ret: list[int] = []
    
    while i < N:
        j, k = i+1, i
        while j < N and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i
            else:
                k += 1
            j += 1
        while i <= k:
            ret.append(i)
            i += j - k
    
    ret.append(N)
    return ret 

if __name__ == "__main__":
    print(Duval_Lyndon_Factorization("ababacaca"))