from dataclasses import dataclass, field

@dataclass
class TrieNode:
    par: int = -1
    char: str = "$"
    next: dict[str, int] = field(default_factory = lambda: {})
    
    def __str__(self):
        return f"<par: {self.par}, char: {self.char}, next: {self.next}>"
    
    @staticmethod
    def trie_add(trie: list['TrieNode'], s: str):
        n = len(trie)
        ptr = 0
        for c in s:
            if c not in trie[ptr].next:
                trie[ptr].next[c] = n
                n += 1
                trie.append(TrieNode(ptr, c))
            ptr = trie[ptr].next[c]

def Trie(SRR: list[str], node_type) -> list:
    if node_type == None:
        node_type = TrieNode
        
    trie = [node_type()]
    for s in SRR:
        node_type.trie_add(trie, s)
    return trie

def simple_trie_add(trie: list[dict[str, int]], s: str):
    n = len(trie)
    ptr = 0
    for c in s:
        if c not in trie[ptr]:
            trie[ptr][c] = n
            n += 1
            trie.append({})
        ptr = trie[ptr][c]

def SimpleTrie(SRR: list[str]) -> list[dict[str, int]]:
    trie = [{}]
    for s in SRR:
        simple_trie_add(trie, s)
    return trie