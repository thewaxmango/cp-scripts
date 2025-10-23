class LazySegTree:
    def __init__(self, n, unit, f, apply, comp, noop):
        self.n = n
        self.unit = unit
        self.noop = noop
        self.f = f
        self.apply = apply
        self.comp = comp
        self.st = [unit] * (2 * n)
        self.lazy = [noop] * (2 * n)
    def __getitem__(self, idx):
        return self.query(idx, idx + 1)
    def __setitem__(self, idx, val):
        self.update(idx, idx + 1, val)
    def build(self, arr):
        for i in range(min(len(arr), self.n)):
            self.st[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.st[i] = self.f(self.st[i * 2], self.st[i * 2 + 1])
    def _push(self, idx, lo, hi):
        if self.lazy[idx] != self.noop:
            self.st[idx] = self.apply(self.st[idx], self.lazy[idx], lo, hi)
            if idx < self.n:
                self.lazy[idx * 2] = self.comp(self.lazy[idx], self.lazy[idx * 2])
                self.lazy[idx * 2 + 1] = self.comp(self.lazy[idx], self.lazy[idx * 2 + 1])
            self.lazy[idx] = self.noop
    def _range_update(self, l, r, val, idx, lo, hi):
        self._push(idx, lo, hi)
        if r <= lo or hi <= l:
            return
        if l <= lo and hi <= r:
            self.lazy[idx] = self.comp(val, self.lazy[idx])
            self._push(idx, lo, hi)
            return
        mid = (lo + hi) // 2
        self._range_update(l, r, val, idx * 2, lo, mid)
        self._range_update(l, r, val, idx * 2 + 1, mid, hi)
        self.st[idx] = self.f(self.st[idx * 2], self.st[idx * 2 + 1])
    def update(self, l, r, val):
        self._range_update(l, r, val, 1, 0, self.n)
    def _range_query(self, l, r, idx, lo, hi):
        self._push(idx, lo, hi)
        if r <= lo or hi <= l:
            return self.unit
        if l <= lo and hi <= r:
            return self.st[idx]
        mid = (lo + hi) // 2
        left_res = self._range_query(l, r, idx * 2, lo, mid)
        right_res = self._range_query(l, r, idx * 2 + 1, mid, hi)
        return self.f(left_res, right_res)
    def query(self, l, r):
        return self._range_query(l, r, 1, 0, self.n)
