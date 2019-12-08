class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def count(self, depth = 1):
        total = len(self.children) * depth 
        for child in self.children:
            total += child.count(depth + 1)

        return total

    def insert(self, orbits):
        childOrbits = list(filter(lambda o: o.parent == self.name, orbits))
        self.children = list(map(lambda o: Node(o.name), childOrbits))
        for child in self.children:
            child.insert(orbits)
        
class Orbit:
    def __init__(self, arg):
        params = arg.split(')')
        self.parent = params[0]
        self.name = params[1]

def run(args):
    orbits = list(map(lambda x: Orbit(x), args))
    com = Node("COM")
    com.insert(orbits)
    return com.count()