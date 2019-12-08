class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
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
            child.parent = self
            child.insert(orbits)

    def get(self, name):
        if self.name == name: return self

        for child in self.children:
            match = child.get(name)
            if match != None: return match

        return None

    def getParents(self):
        if self.parent == None: return []
        
        parents = self.parent.getParents()
        parents.append(self.parent)
        return parents
        
class Orbit:
    def __init__(self, arg):
        params = arg.split(')')
        self.parent = params[0]
        self.name = params[1]

def run(args):
    orbits = list(map(lambda x: Orbit(x), args))
    com = Node('COM')
    com.insert(orbits)
    yparents = com.get('YOU').getParents()
    sparents = com.get('SAN').getParents()
    yparents.reverse()
    sparents.reverse()
    i = 0
    for yp in yparents:
        j = 0
        for sp in sparents:
            if sp.name == yp.name: return i + j
            j += 1
        i += 1

    return -1