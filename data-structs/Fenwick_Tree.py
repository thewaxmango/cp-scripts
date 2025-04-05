# FROM PYRIVAL
# with some added methods

class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1
    
    def update_range(self, left, right, x):
        self.update(left, x)
        self.update(right, -x)

    def query(self, right):
        """calc sum(bit[:right])"""
        x = 0
        while right:
            x += self.bit[right - 1]
            right &= right - 1
        return x
    
    def query_range(self, left, right):
        return self.query(right) - self.query(left)

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1