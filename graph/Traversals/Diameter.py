# return: [index, distance]
def furthest(adjl: list[set[int]], x: int) -> tuple[int, int]:
    q, d = [0], [-1]*len(adjl)
    d[x] = 0
    while q:
        for j in adjl[(i := q.pop())]:
            if d[j] == None:
                d[j] = d[i] + 1
                q.append(j)
    return max(enumerate(d), key=lambda x:x[1])

# return: path
def furthest_path(adjl: list[set[int]], x: int) -> list[int]:
    q, d, p = [0], [-1]*len(adjl), [-1]*len(adjl)
    d[x] = 0
    while q:
        for j in adjl[(i := q.pop())]:
            if d[j] == None:
                d[j], p[j] = d[i] + 1, i
                q.append(j)
    z = max(range(len(d)), key=d.__getitem__)
    a = []
    while z != -1:
        a.append(z)
        z = p[z]
    return a[::-1]

# return: [index1, index2, distance]
def diameter(adjl: list[set[int]]) -> tuple[int, int, int]:
    z, _ = furthest(adjl, 0)
    y, yd = furthest(adjl, z)
    return (y, z, yd)

def diameter_path(adjl: list[set[int]]) -> list[int]:
    p1 = furthest_path(adjl, 0)
    return furthest_path(adjl, p1[-1])