from Z_Algorithm import Z
from Suffix_Array_Class import SuffixArray
# returns length, start, end (not inclusive)

# Translated from USACO GUIDE
# gives strict repetitions (no overflow e.g. abcabca)
def Strict_Main_Lorentz(_s: str) -> list[tuple[int, int, int]]:
    def get_z(Z: list[int], idx: int) -> int:
        if 0 <= idx < len(Z):
            return Z[idx]
        return 0
    
    repetitions: list[tuple[int, int, int]] = []
    
    # O(n^2) generates actual pairs
    def convert_to_repetitions(shift: int, left: bool, cntr: int, l: int, k1: int, k2: int) -> None:
        nonlocal repetitions
        for l1 in range(max(1, l - k2), min(l, k1) + 1):
            if left and l1 == l:
                break
            l2: int = l - l1
            pos: int = shift + (cntr - l1 if left else cntr - l - l1 + 1)
            repetitions.append((l1 + l2, pos, pos + 2 * l))
    
    def find_repetitions(S: str, shift: int = 0) -> None:        
        N: int = len(S)
        if N == 1:
            return
        
        nu: int = N // 2
        nv: int = N - nu
        u: str = S[:nu]
        v: str = S[nu:]
        ru: str = u[::-1]
        rv: str = v[::-1]
        
        find_repetitions(u, shift)
        find_repetitions(v, shift + nu)
        
        z1: list[int] = Z(ru)
        z2: list[int] = Z(v + '#' + u)
        z3: list[int] = Z(ru + '#' + rv)
        z4: list[int] = Z(v)
        
        for cntr in range(0, N):
            l: int
            k1: int
            k2: int
            
            if cntr < nu:
                l = nu - cntr
                k1 = get_z(z1, nu - cntr)
                k2 = get_z(z2, nv + 1 + cntr)
            else:
                l = cntr - nu + 1
                k1 = get_z(z3, nu + 1 + nv - 1 - (cntr - nu))
                k2 = get_z(z4, (cntr - nu) + 1)
            
            if k1 + k2 >= l:
                convert_to_repetitions(shift, cntr < nu, cntr, l, k1, k2)
                
    find_repetitions(_s)
    return repetitions

# From YOSUPO JUDGE solution
# not strict repetitions, can overflow but eliminates overlap
def Run_Enumerate(S: str) -> list[tuple[int, int, int]]:
    n = len(S)
    sa = SuffixArray(S)
    sa_rev = SuffixArray(S[::-1])
    runs = []
    vis = set()
    lst = -1
    for p in range(1, n // 2 + 1):
        for i in range(0, n - p + 1, p):
            l = i - sa_rev.get_lcp(n - i - p, n - i)
            r = i - p + sa.get_lcp(i, i + p)
            if l > r or l == lst:
                continue
            if (l, r + 2 * p) not in vis:
                vis.add((l, r + 2 * p))
                runs.append((p, l, r + 2 * p))
            lst = l
    return runs

for tup in Run_Enumerate("mississipppi"):
    print(*tup)
    
for tup in Strict_Main_Lorentz("mississipppi"):
    print(*tup)