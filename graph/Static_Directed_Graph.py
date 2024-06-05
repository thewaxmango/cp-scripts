class StaticDirectedGraph:
    def __init__(self, size):
        self.size = size
        self.adjacents = [set() for _ in range(size)]
    
    def add_edge(self, parent, child):
        self.adjacents[parent].add(child)
    
    def remove_edge(self, parent, child):
        self.adjacents[parent].remove(child)

