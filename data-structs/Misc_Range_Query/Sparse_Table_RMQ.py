# range minimum query
def build_rmq(array):
    m, l = max(array), len(array)
    sparse_table = [[float('inf')] * (l + 1 - (1 << i)) for i in range(m.bit_length())]
    sparse_table[0] = array.copy()
    
    for i in range(1, m.bit_length() + 1):        
        for j in range(l + 1 - (1 << i)):
            sparse_table[i][j] = min(sparse_table[i - 1][j], sparse_table[i - 1][j + (1 << (i - 1))])
    
    return sparse_table

# r not inclusive
def get_rmq(sparse_table, l, r):
    b = (r - l).bit_length() - 1
    d = 1 << b
    return min(sparse_table[b][l], sparse_table[b][r - d])
    
# from yosupo judge, lacks online functionality
class SparseTable:
    def __init__(self, arr, op=min):
        self.op = op
        self.n = len(arr)
        self.h = self.n.bit_length() - 1
        self.table = [[0] * self.n for _ in range(self.h + 1)]
        self.table[0] = [a for a in arr]
        for k in range(self.h):
            nxt, prv = self.table[k + 1], self.table[k]
            l = 1 << k
            for i in range(self.n - l * 2 + 1):
                nxt[i] = op(prv[i], prv[i + l])

    def prod(self, l, r):
        assert 0 <= l < r <= self.n
        k = (r - l).bit_length() - 1
        return self.op(self.table[k][l], self.table[k][r - (1 << k)])

arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
st = build_rmq(arr)
print(get_rmq(st, 4, 6))