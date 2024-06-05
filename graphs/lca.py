# --- SPARSETABLE.PY --------------------------------------------------------------------------------------------s

# range minimum query
def build_rmq(array):
    m, l = max(array), len(array)
    sparse_table = [[float('inf')] * (l + 1 - (1 << i)) for i in range(m.bit_length())]
    sparse_table[0] = array.copy()
    
    for i in range(1, m.bit_length() + 1):        
        for j in range(l + 1 - (1 << i)):
            sparse_table[i][j] = min(sparse_table[i - 1][j], sparse_table[i - 1][j + (1 << (i - 1))])
    
    return sparse_table

# r not inclusive
def get_rmq(sparse_table, l, r):
    b = (r - l).bit_length() - 1
    d = 1 << b
    return min(sparse_table[b][l], sparse_table[b][r - d])

# --------------------------------------------------------------------------------------------------------------


def build_lca_from_adjlist(adjlist, root: int) -> list[tuple[int, int]]:    
    if len(adjlist) == 1:
        return [(0, root)]
    
    def helper(adjlist, root: int, parent: int, depth: int) -> list[tuple[int, int]]:
        if len(adjlist[root]) == 1:
            return [(depth, root)]
        
        output: list[tuple[int, int]] = [(depth, root)]
        for child in adjlist[root]:
            if child == parent:
                continue
            output += helper(adjlist, child, root, depth + 1) 
            output.append((depth, root))
        return output
    
    output: list[tuple[int, int]] = [(0, root)]
    for child in adjlist[root]:
        output += helper(adjlist, child, root, 1) 
        output.append((0, root))
    
    return output

def build_lca_from_bst():
    pass

def get_lca():
    pass