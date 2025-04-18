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
