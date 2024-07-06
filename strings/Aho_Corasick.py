from dataclasses import dataclass, field
from collections import deque
from Trie import Trie

@dataclass
class AhoCorasickNode:
    par: int = -1
    char: str = "$"
    next: dict[str, int] = field(default_factory = lambda: {})
    link: int = -1
    
    def __str__(self):
        return f"<par: {self.par}, char: {self.char}, link: {self.link}, next: {self.next}>"
    
    @staticmethod
    def trie_add(trie: list['AhoCorasickNode'], s: str):
        n = len(trie)
        ptr = 0
        for c in s:
            if c not in trie[ptr].next:
                trie[ptr].next[c] = n
                n += 1
                trie.append(AhoCorasickNode(ptr, c))
            ptr = trie[ptr].next[c]

# builds links for aho corasick
def AhoCorasick(trie: list[AhoCorasickNode]):
    dq = deque(trie[0].next.values())
    for i in trie[0].next.values():
        trie[i].link = 0
    
    while dq:
        v: int = dq.popleft()   
        for c, u in trie[v].next.items():
            dq.append(u)
                
            j: int = trie[v].link
            while trie[j].link != -1 and c not in trie[j].next:
                j = trie[j].link
            trie[u].link = trie[j].next[c] 

words = ["a", "ag", "c", "caa", "gag", "gc", "gca"]
trie = Trie(words, AhoCorasickNode)
AhoCorasick(trie)
print(*trie, sep="\n")