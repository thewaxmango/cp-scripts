# PyRival SCC, returns in topolgical order
def tarjan(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)
 
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]


# strongly connected components (alternative to Kosaraju and path-based)
def tarjan_recursive(adjs):
    size = len(adjs)
    index = [None]*size
    lowlink = [None]*size
    on_stack = [False]*size

    idx = 0
    stack = []
    output = []

    def connect(i):
        nonlocal idx
    
        index[i] = idx
        lowlink[i] = idx
        idx = idx + 1
        stack.append(i)
        on_stack[i] = True
    
        for j in adjs[i]:
            if index[j] == None:
                connect(j)
                lowlink[i] = min(lowlink[i], lowlink[j])
            elif on_stack[j]:
                lowlink[i] = min(lowlink[i], index[j])
        
        if lowlink[i] == index[i]:
            output.append([])
            
            j = None
            while i != j:
                j = stack.pop()
                on_stack[j] = False
                output[-1].append(j)
            
    for i in range(size):
        if index[i] == None:
            connect(i)
    
    return output