class Program:
    def __init__(self, source = []):
        self.source = source
        self.inputs = []
        self.outputs = []
        self.end = False
        self.i = 0
        self.b = 0

    def run(self):
        self.outputs = []
        while True:
            opcode = self.source[self.i] % 100
            if opcode == 1: self.add()
            if opcode == 2: self.multiply()
            if opcode == 3:
                if len(self.inputs) == 0: return 
                self.input()
            if opcode == 4: self.output()
            if opcode == 5: self.jumpIfTrue()
            if opcode == 6: self.jumpIfFalse()
            if opcode == 7: self.lessThan()
            if opcode == 8: self.equals()
            if opcode == 9: self.relativeBase()
            if opcode == 99: 
                self.end = True
                return

    def getModes(self, n):
        opcode = str(self.source[self.i]).zfill(n)[0:n-2]
        modes = list(map(lambda x: int(x), opcode))
        modes.reverse()
        return modes

    def move(self, n):
        self.i = self.i + n

    def getAddresses(self, n):
        modes = self.getModes(n + 2)
        for m in range(0, n):
            i = self.i + m + 1
            if modes[m] == 1: yield i
            elif modes[m] == 2: yield self.getAt(i) + self.b
            else: yield self.getAt(i)

    def getValues(self, addresses):
        for address in addresses:
            yield self.getAt(address)

    def getAt(self, i):
        self.grow(i)
        return self.source[i]

    def setAt(self, i, v):
        self.grow(i)
        self.source[i] = v

    def grow(self, i):
        n = i - len(self.source) + 1
        if n <= 0: return
        self.source += list(0 for x in range(0, n))

    def add(self):
        a = list(self.getAddresses(3))
        v = list(self.getValues(a[0:2]))
        self.setAt(a[2], v[0] + v[1])
        self.move(4)

    def multiply(self):
        a = list(self.getAddresses(3))
        v = list(self.getValues(a[0:2]))
        self.setAt(a[2], v[0] * v[1])
        self.move(4)

    def input(self):
        a = list(self.getAddresses(1))
        self.setAt(a[0], self.inputs.pop(0))
        self.move(2)

    def output(self):
        a = list(self.getAddresses(1))
        v = self.getAt(a[0])
        self.outputs.append(v)
        self.move(2)

    def jumpIfTrue(self):
        a = list(self.getAddresses(2))
        v = list(self.getValues(a))
        if v[0] != 0: self.i = v[1]
        else: self.move(3)

    def jumpIfFalse(self):
        a = list(self.getAddresses(2))
        v = list(self.getValues(a))
        if v[0] == 0: self.i = v[1]
        else: self.move(3)
        
    def lessThan(self):
        a = list(self.getAddresses(3))
        v = list(self.getValues(a[0:2]))
        self.setAt(a[2], 1 if v[0] < v[1] else 0)
        self.move(4)
        
    def equals(self):
        a = list(self.getAddresses(3))
        v = list(self.getValues(a[0:2]))
        self.setAt(a[2], 1 if v[0] == v[1] else 0)
        self.move(4)

    def relativeBase(self):
        a = list(self.getAddresses(1))
        self.b += self.getAt(a[0])
        self.move(2)