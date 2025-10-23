from dataclasses import dataclass, field

@dataclass
class Node:
    ln: int
    link: int = -1
    nxt: dict[str, int] = field(default_factory=dict)

class SuffixAutomaton:
    def __init__(self, s: str = "") -> None:
        self.st: list[Node] = [Node(0, -1)]
        self.last: int = 0
        self.extend(s)
    def extend(self, s: str) -> None:
        for ch in s:
            self.extend_ch(ch)
    def extend_ch(self, ch: str) -> None:
        cur: int = len(self.st)
        self.st.append(Node(self.st[self.last].ln + 1))
        p: int = self.last
        while p != -1 and ch not in self.st[p].nxt:
            self.st[p].nxt[ch] = cur
            p = self.st[p].link
        if p == -1:
            self.st[cur].link = 0
        else:
            q: int = self.st[p].nxt[ch]
            if self.st[p].ln + 1 == self.st[q].ln:
                self.st[cur].link = q
            else:
                clone: int = len(self.st)
                self.st.append(Node(self.st[p].ln+1,
                                    self.st[q].link,
                                    self.st[q].nxt.copy()))
                while p != -1 and self.st[p].nxt[ch] == q:
                    self.st[p].nxt[ch] = clone
                    p = self.st[p].link
                self.st[q].link = self.st[cur].link = clone
        self.last = cur
