# FROM PYRIVAL
# with some added methods

# https://cp-algorithms.com/data_structures/fenwick.html#1-point-update-and-range-query
# 1. point update, range query
# 2. range update, point query
# 3. range update, range query

class FenwickTree:
    def __init__(self, n=-1, x=None):
        if x == None:
            self.bit = [0]*n
        else:
            self.bit = x
            for i in range(len(x)):
                j = i | (i + 1)
                if j < len(x):
                    x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1
    
    # [0:right]
    def query(self, right):
        x = 0
        while right:
            x += self.bit[right - 1]
            right &= right - 1
        return x
    
    def query_range(self, left, right):
        return self.query(right) - self.query(left)
    
    # usually not used with update
    def update_range(self, left, right, x):
        self.update(left, x)
        self.update(right, -x)

    # find max idx s.t. sum(bit[:idx]) <= k
    def findkth(self, k):
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1