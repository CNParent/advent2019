import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getCheckpoints(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        d = math.gcd(dx, dy)
        if d == 1: return []

        dx = int(dx / d if d != 0 else 0)
        dy = int(dy / d if d != 0 else 0)
        x = self.x + dx
        y = self.y + dy
        while x != other.x or y != other.y:
            yield Point(x, y)
            x += dx
            y += dy

    def equals(self, other):
        return self.x == other.x and self.y == other.y

class StationLocation:
    def __init__(self, p, n):
        self.p = p
        self.n = n

class Field:
    def __init__(self, data):
        self.data = data
        self.w = len(data[0])
        self.h = len(data)

    def get(self, p = Point(0, 0)):
        #print(f'Getting [{p.x},{p.y}]')
        #print(f'[{p.y}]={self.data[p.y]}')
        #print(f'[{p.x}]={self.data[p.y][p.x]}')
        return self.data[p.y][p.x]

    def getMaxVisibility(self):
        locations = []
        for i in range(0, self.w):
            for j in range(0, self.h):
                p = Point(i, j)
                if self.get(p) == '.': continue
                locations.append(self.getVisibleFrom(p))

        return max(locations, key = lambda x: x.n)

    def getVisibleFrom(self, p = Point(0, 0)):
        total = 0
        for i in range(0, self.w):
            for j in range(0, self.h):
                o = Point(i, j)
                if self.get(o) == '#' and self.canSee(p, o):
                    total += 1

        return StationLocation(p, total)

    def canSee(self, p1, p2):
        if p1.equals(p2): return False

        checkpoints = list(p1.getCheckpoints(p2))
        for p in checkpoints:
            if self.get(p) == '#': return False

        return True


def run(args):
    f = Field(args)
    s = f.getMaxVisibility()
    return f'Station at [{s.p.x},{s.p.y}] with visibility {s.n}'