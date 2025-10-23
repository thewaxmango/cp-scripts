# dfs
def topological_sort(adjs):
    size = len(adjs)
    visited = [False]*size
    dfs = []
    post_order = []
    
    for i in range(size):
        if not visited[i]:
            dfs.append((False, i))
        
        while dfs:
            node = dfs.pop()
            if node[0]:
                post_order.append(node[1])
                continue
            if visited[node[1]]:
                continue
            
            visited[node[1]] = True
            dfs.append((True, node[1]))
            for child in adjs[node[1]]:
                if not visited[child]:
                    dfs.append((False, child))
    
    return post_order

# dfs faster??
def topological_sort2(adjs):
    size = len(adjs)
    visited = [False]*size
    dfs = []
    post_order = []
    
    for i in range(size):
        if not visited[i]:
            dfs.append(~i)
        
        while dfs:
            i = ~dfs.pop()
            if i < 0:
                post_order.append(~i)
                continue
            if visited[i]:
                continue
            
            visited[i] = True
            dfs.append(i)
            for j in adjs[i]:
                if not visited[j]:
                    dfs.append(~j)
    
    return post_order

# smdbs's bfs
from collections import deque

def topologicalSort(g):
    # g: adj list
    n = len(g)
    indeg = [0] * n
    for i in range(n):
        for v in g[i]:
            indeg[v] += 1
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    ans = []
    
    while q:
        i = q.popleft()
        ans.append(i)
        for v in g[i]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return ans

def topological_sort_recursive(adjs):
    size = len(adjs)
    perm_mark = [False]*size
    temp_mark = [False]*size
    unmarked = set(range(size))
    output = []
    
    def visit(i):
        if perm_mark[i]:
            return False
        if temp_mark[i]:
            return True
    
        temp_mark[i] = True
        unmarked.remove(i)
        for j in adjs[i]:
            if visit(j):
                return True
            
        temp_mark[i] = False
        perm_mark[i] = True
        output.append(i)
        return False
    
    while unmarked:
        if visit(next(iter(unmarked))):
            return None
    
    return output[::-1]

a = [[1],[2],[0]]
print(topological_sort(a))
print(topological_sort2(a))