class Graph:
    def __init__(self):
        self.adjacents = {}
    
    def add_node(self, name, adjacents = []):
        if name in self.nodes:
            return False
        self.adjacents[name] = set(adjacents)
        return True
    
    def add_edge(self, name1, name2):
        if name1 not in self.nodes or name2 not in self.nodes:
            return False
        if name2 in self.adjacents[name1]:
            return False
        self.adjacents[name1].add(name2)
        self.adjacents[name2].add(name1)
        return True
    
    def remove_edge(self, name1, name2):
        if name1 not in self.nodes or name2 not in self.nodes:
            return False
        if name2 not in self.adjacents[name1]:
            return False
        self.adjacents[name1].remove(name2)
        self.adjacents[name2].remove(name1)
        return True


    