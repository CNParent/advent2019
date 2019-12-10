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

    def angleTo(self, other):
        x = other.x - self.x 
        y = other.y - self.y
        if x >= 0 and y < 0: return math.atan(abs(x / y))
        elif x > 0 and y >= 0: return math.atan(abs(y / x)) + math.pi * 0.5
        elif x <= 0 and y > 0: return math.atan(abs(x / y)) + math.pi
        elif x < 0 and y <= 0: return math.atan(abs(y / x)) + math.pi * 1.5
        return 0.0

class StationLocation:
    def __init__(self, p, v):
        self.p = p
        self.v = v

class Field:
    def __init__(self, data):
        self.data = data
        self.w = len(data[0])
        self.h = len(data)
        self.destroyed = []

    def get(self, p):
        return self.data[p.y][p.x]

    def clearAt(self, p):
        self.data[p.y][p.x] = '.'

    def clearAsteroidsFrom(self, s):
        while len(s.v) != 0:
            next = min(s.v, key = lambda p: s.p.angleTo(p))
            self.destroyed.append(next)
            self.clearAt(next)
            s.v.remove(next)

        s.v = list(self.getVisibleFrom(s.p))


    def getMaxVisibility(self):
        locations = []
        for i in range(0, self.w):
            for j in range(0, self.h):
                p = Point(i, j)
                if self.get(p) == '.': continue
                v = list(self.getVisibleFrom(p))
                locations.append(StationLocation(p, v))

        return max(locations, key = lambda x: len(x.v))

    def getVisibleFrom(self, p = Point(0, 0)):
        for i in range(0, self.w):
            for j in range(0, self.h):
                o = Point(i, j)
                if self.get(o) == '#' and self.canSee(p, o):
                    yield o

    def canSee(self, p1, p2):
        if p1.equals(p2): return False

        checkpoints = list(p1.getCheckpoints(p2))
        for p in checkpoints:
            if self.get(p) == '#': return False

        return True

def run(args):
    f = partTwo(args)
    a = f.destroyed[199]
    return a.x * 100 + a.y

def partTwo(args):
    data = list(map(lambda r: list(map(lambda i: i, r)), args))
    f = Field(data)
    s = f.getMaxVisibility()
    while len(s.v) != 0:
        f.clearAsteroidsFrom(s)

    return f

def partOne(args):
    f = Field(args)
    s = f.getMaxVisibility()
    return f'Station at [{s.p.x},{s.p.y}] with visibility {len(s.v)}'