# COMPLETE

from dataclasses import dataclass, field

MAXN = 10**5

def suffix_tree(s: str):
    @dataclass
    class Node:
        l: int = 0
        r: int = 0
        par: int = -1
        link: int = -1
        next: dict[str, int] = field(default_factory = lambda: {})
        
        def __str__(self):
            return f"<l: {self.l}, r: {self.r}, par: {self.par}, link: {self.link}, next: {self.next}>"
        
        def len(self) -> int:
            return self.r - self.l
        
        def get(self, c: str) -> int:
            if c not in self.next:
                self.next[c] = -1
            return self.next[c]
    
    @dataclass
    class State:
        v: int
        pos: int
        
    n: int = len(s)
    t: list[Node] = [Node() for _ in range(MAXN)]
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
    
def suffix_tree_compressed(s):
    pass

print(suffix_tree("abcabxabcd"))