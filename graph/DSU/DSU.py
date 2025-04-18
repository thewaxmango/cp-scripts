# source: usaco.guide

class DSU:
	def __init__(self, size: int) -> None:
		self.parents = [-1 for _ in range(size)]
		self.sizes = [1 for _ in range(size)]

	# finds the "representative" node in a's component
	def find(self, x: int) -> int:
		if self.parents[x] == -1:
			return x
		self.parents[x] = self.find(self.parents[x])
		return self.parents[x]

	# returns whether the merge changed connectivity
	def union(self, x: int, y: int) -> bool:
		x_root, y_root = self.find(x), self.find(y)
		if x_root == y_root:
			return False
		if self.sizes[x_root] < self.sizes[y_root]:
			x_root, y_root = y_root, x_root
		self.parents[y_root] = x_root
		self.sizes[x_root] += self.sizes[y_root]
		return True

	# returns whether two nodes are in the same connected component
	def connected(self, x: int, y: int) -> bool:
		return self.find(x) == self.find(y)