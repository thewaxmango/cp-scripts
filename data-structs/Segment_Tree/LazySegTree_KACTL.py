class LazySegNode:
    __slots__ = ('l', 'r', 'lo', 'hi', 'f', 'unit', 'apply', 'comp', 'noop', 'lazy')
    def __init__(self, lo, hi, *, f, unit, apply, comp, noop, arr=None):
        self.l = self.r = None
        self.lo, self.hi = lo, hi
        self.f = f
        self.unit = unit
        self.apply = apply
        self.comp = comp
        self.noop = noop
        self.lazy = noop
        if arr is not None:
            if lo + 1 < hi:
                mid = (lo + hi) // 2
                self.l = LazySegNode(lo, mid, f=f, unit=unit, apply=apply, comp=comp, noop=noop, arr=arr)
                self.r = LazySegNode(mid, hi, f=f, unit=unit, apply=apply, comp=comp, noop=noop, arr=arr)
                self.val = f(self.l.val, self.r.val)
            else:
                self.val = arr[lo]
        else:
            self.val = unit
    def _ensure_children(self):
        if not self.l:
            mid = (self.lo + self.hi) // 2
            self.l = LazySegNode(self.lo, mid, f=self.f, unit=self.unit,
                                 apply=self.apply, comp=self.comp, noop=self.noop)
            self.r = LazySegNode(mid, self.hi, f=self.f, unit=self.unit,
                                 apply=self.apply, comp=self.comp, noop=self.noop)
    def _push(self):
        if self.lazy == self.noop:
            return
        self._ensure_children()
        for child in (self.l, self.r):
            child.val = self.apply(child.val, self.lazy, child.lo, child.hi)
            child.lazy = self.comp(self.lazy, child.lazy)
        self.lazy = self.noop
    def query(self, L, R):
        if R <= self.lo or self.hi <= L:
            return self.unit
        if L <= self.lo and self.hi <= R:
            return self.val
        self._push()
        return self.f(self.l.query(L, R), self.r.query(L, R))
    def update(self, L, R, update_val):
        if R <= self.lo or self.hi <= L:
            return
        if L <= self.lo and self.hi <= R:
            self.val = self.apply(self.val, update_val, self.lo, self.hi)
            self.lazy = self.comp(update_val, self.lazy)
        else:
            self._push()
            self.l.update(L, R, update_val)
            self.r.update(L, R, update_val)
            self.val = self.f(self.l.val, self.r.val)
