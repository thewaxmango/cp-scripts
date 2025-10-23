from sortedcontainers import SortedList

class OrderStatisticTree:
    def __init__(self):
        self.tree = SortedList()

    def insert(self, x):
        self.tree.add(x)

    def delete(self, x):
        if x in self.tree:
            self.tree.remove(x)
            return True
        return False

    def select(self, k):
        if 0 <= k < len(self.tree):
            return self.tree[k]
        return None

    def rank(self, x):
        """Returns the number of elements < x (rank of x)."""
        return self.tree.bisect_left(x)