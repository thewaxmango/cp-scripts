# Suffix Array translated from CP-ALGORITHMS
# Generalized coded by me

from dataclasses import dataclass, field
from bisect import bisect_left as bsl

@dataclass
class Node:
    l: int = 0
    r: int = 0
    par: int = -1
    link: int = -1
    next: dict[str, int] = field(default_factory = lambda: {})
    
    # for generalized may want to add data regarding which strings contain
    
    def __str__(self):
        return f"<l: {self.l}, r: {self.r}, par: {self.par}, link: {self.link}, next: {self.next}>"
    
    def len(self) -> int:
        return self.r - self.l
    
    def get(self, c: str) -> int:
        if c not in self.next:
            self.next[c] = -1
        return self.next[c]

def Suffix_Tree(s: str): 
    @dataclass
    class State:
        v: int
        pos: int

    s += "$"
    n: int = len(s)
    t: list[Node] = [Node() for _ in range(2*n)]
    sz: int = 1
    ptr: State = State(0, 0)
    
    def go(st: State, l: int, r: int) -> State: 
        nonlocal s, t
        while (l < r):
            if st.pos == t[st.v].len():
                st = State(t[st.v].get(s[l]), 0)
                if (st.v == -1):
                    return st
            else:
                if (s[t[st.v].l + st.pos] != s[l]):
                    return State(-1, -1)
                if (r - l < t[st.v].len() - st.pos):
                    return State(st.v, st.pos + r - l)
                l += t[st.v].len() - st.pos
                st.pos = t[st.v].len()
        return st
    
    def split(st: State) -> int:
        nonlocal s, t, sz
        if (st.pos == t[st.v].len()):
            return st.v
        if (st.pos == 0):
            return t[st.v].par
        
        v: Node = t[st.v]
        id: int = sz
        sz += 1
        
        t[id] = Node(v.l, v.l + st.pos, v.par)
        t[v.par].next[s[v.l]] = id
        t[id].next[s[v.l + st.pos]] = st.v
        t[st.v].par = id
        t[st.v].l += st.pos
        return id
    
    def get_link(v: int) -> int:
        nonlocal t
        if (t[v].link != -1):
            return t[v].link
        if (t[v].par == -1):
            return 0
        
        to: int = get_link(t[v].par)
        t[v].link = split(go(State(to, t[to].len()), t[v].l + int(t[v].par == 0), t[v].r))
        return t[v].link
    
    def tree_extend(pos: int) -> None:
        nonlocal s, n, t, sz, ptr
        while(True):
            nptr: State = go(ptr, pos, pos+1)
            if (nptr.v != -1):
                ptr = nptr
                return

            mid: int = split(ptr)
            leaf: int = sz
            sz += 1
            t[leaf] = Node(pos, n, mid)
            t[mid].next[s[pos]] = leaf

            ptr.v = get_link(mid)
            ptr.pos = t[ptr.v].len()
            if (not mid):
                break
            
    for i in range(n):
        tree_extend(i)
    
    return t[:sz]

# don't use suffix tree to construct suffix array unless you have to
def Suffix_Tree_To_Array(S: str, ST: list[Node]) -> list[int]:
    S += "$"
    N = len(S)
    ret: list[int] = []
    
    s_dict: dict[int, int] = {-1: 0}
    stack: list[int] = [0]
    
    while stack:
        idx: int = stack.pop()
        node: Node = ST[idx]
        
        s_dict[idx] = s_dict[node.par] - node.l + node.r
        if node.next:
            stack += [v for _k, v in sorted(node.next.items(), reverse=True)]
        else:
            ret.append(N - s_dict[idx])
    
    return ret[1:]

def Generalized_Suffix_Tree(SRR: list[str]):
    S: str = "$".join(SRR)
    ST: list[Node] = Suffix_Tree(S)
    
    sentinels: list[int] = [i for i, c in enumerate(S) if c == "$"] + [len(S)]
    for node in ST:
        l_sentinel = bsl(sentinels, node.l)
        r_sentinel = bsl(sentinels, node.r - 1)
        
        # if crosses a sentinel, prune edge and children
        if l_sentinel != r_sentinel:
            node.next = {}
            node.r = sentinels[l_sentinel] + 1
            continue
        
        # if ends on a sentinel, prune children
        if node.r == sentinels[r_sentinel] + 1:
            node.next = {}
    
    return ST

def Compact_Sort_ST(ST: list[Node]):    
    sz: int = 0
    cst: list[Node] = []
    
    stack: list[tuple[str, int]] = [("", 0)]
    while stack:
        edge_char, old_idx = stack.pop()
        new_idx = sz
        sz += 1
        
        node = ST[old_idx]
        cst.append(node)
        if node.par != -1:
            cst[node.par].next[edge_char] = new_idx
        
        for c, v in sorted(node.next.items(), reverse=True):
            # add old and new idx to stack
            stack.append((c, v))
            ST[v].par = new_idx
    
    return cst

if __name__ == "__main__":
    s1 = "bacabadabcaba"
    s2 = "abracadabra"
    s3 = "acbadabraca"
    s4 = "mississippi"
    s = [s1, s2, s3]
    st = Suffix_Tree(s4)
    #print(len(st))
    print(*st, sep="\n")
    print()
    #cst = Compact_Sort_ST(st)
    #print(len(cst))
    #print(*cst, sep="\n")