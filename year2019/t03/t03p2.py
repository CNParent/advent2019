class instruction:
    def __init__(self, text):
        self.up = text[0] == 'U'
        self.down = text[0] == 'D'
        self.right = text[0] == 'R'
        self.left = text[0] == 'L'
        self.delta = int(text[1:len(text)])

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.steps = 0

    def isOrigin(self):
        return self.distance() == 0

    def distance(self):
        return abs(self.x) + abs(self.y)

    def stepsFrom(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def isHorizontal(self):
        return self.p1.y == self.p2.y

    def isVertical(self):
        return self.p1.x == self.p2.x

    def minabsX(self):
        return min([abs(self.p1.x), abs(self.p2.x)])

    def minabsY(self):
        return min([abs(self.p1.y), abs(self.p2.y)])

    def maxX(self):
        return self.p1.x if self.p1.x > self.p2.x else self.p2.x

    def minX(self):
        return self.p1.x if self.p1.x < self.p2.x else self.p2.x

    def maxY(self):
        return self.p1.y if self.p1.y > self.p2.y else self.p2.y
    
    def minY(self):
        return self.p1.y if self.p1.y < self.p2.y else self.p2.y

    def isParallelTo(self, other):
        return (self.isHorizontal() and other.isHorizontal()) or (self.isVertical() and other.isVertical())

    def xCrosses(self, other):
        return not (other.maxX() <= self.minX() or other.minX() >= self.maxX())

    def yCrosses(self, other):
        return not (other.maxY() <= self.minY() or other.minY() >= self.maxY())

    def intersects(self, other):
        return self.xCrosses(other) and self.yCrosses(other)
    
    def intersection(self, other):
        if not self.isParallelTo(other):
            x = self.p1.x if self.isVertical() else other.p1.x
            y = self.p1.y if self.isHorizontal() else other.p1.y
        else:
            x = self.minabsX() if self.minabsX() < other.minabsX() else other.minabsX()
            y = self.minabsY() if self.minabsY() < other.minabsY() else other.minabsY()

        p = point(x,y)
        p.steps = self.p1.steps + other.p1.steps + self.p1.stepsFrom(p) + other.p1.stepsFrom(p)
        return p


def getLines(instructions):
    p1 = point(0,0)
    lines = []
    for i in instructions:
        if i.up: p2 = point(p1.x, p1.y + i.delta)
        if i.down: p2 = point(p1.x, p1.y - i.delta)
        if i.right: p2 = point(p1.x + i.delta, p1.y)
        if i.left: p2 = point(p1.x - i.delta, p1.y)

        p2.steps = p1.steps + i.delta
        lines.append(line(p1,p2))
        p1 = p2
    
    return lines

def run(args):
    linesa = getLines(map(lambda x: instruction(x), args[0].split(',')))
    linesb = getLines(map(lambda x: instruction(x), args[1].split(',')))
    intersections = []
    for linea in linesa:
        for lineb in linesb:
            if linea.intersects(lineb): 
                p = linea.intersection(lineb)
                if p.isOrigin(): continue
                intersections.append(p)

    steps = map(lambda x: x.steps, intersections)
    return min(steps)