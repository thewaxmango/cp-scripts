# returns: (list-in, list-out) of indices [0, 2n)
def euler_tour(adjl: list[set[int]], root: int) -> tuple[list[int], list[int]]:
    q, ein, eout, c = [root], [-1]*len(adjl), [-1]*len(adjl), 0
    while q:
        if (n := q.pop()) >= 0:
            ein[n] = c
            q.append(~n)
        else:
            eout[~n] = c
        c += 1
    return ein, eout