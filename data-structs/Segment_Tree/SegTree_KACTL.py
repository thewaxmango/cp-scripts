class SegTree:
    def __init__(self, n: int, unit, f) -> None:
        self.n = n
        self.unit = unit
        self.st = [unit]*(n*2)
        self.f = f
    def __getitem__(self, idx: int): return self.st[idx + self.n]
    def __setitem__(self, idx: int, val): self.update(idx, val)
    def build(self, arr: list):
        self.st[self.n:] = arr
        for idx in range(self.n-1, -1, -1):
            self.st[idx] = self.f(self.st[idx*2], self.st[idx*2+1])
    def update(self, idx: int, val) -> None:
        idx += self.n
        self.st[idx] = val
        while (idx := idx // 2):
            self.st[idx] = self.f(self.st[idx*2], self.st[idx*2+1])
    def query(self, l: int, r: int): # right-exclusive
        ra, rb = self.unit, self.unit
        l, r = l + self.n, r + self.n 
        while l < r:
            if l % 2: 
                ra = self.f(ra, self.st[l])
            if r % 2:
                r -= 1
                rb = self.f(self.st[r], rb)
            l, r = (l + 1) // 2, r // 2
        return self.f(ra, rb)

    
# verification on yosupo
# https://judge.yosupo.jp/submission/279834
def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    st = SegTree(n, 0, lambda x, y: x + y)
    st.build(a)
    for _ in range(q):
        m, j, k = map(int, input().split())
        if m == 0:
            st.update(j, st[j]+k)
        else:
            print(st.query(j, k))

if __name__ == "__main__":
    main()
