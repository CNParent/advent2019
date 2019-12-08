class Result:
    def __init__(self, error, nexti):
        self.error = error
        self.nexti = nexti

class Command:
    def __init__(self, values, i):
        cmd = values[i]
        l = len(cmd)
        if l < 3:
            opcode = int(cmd)
            self.pmodes = []
        else:
            opStr = cmd[l-2:l]
            pmodesStr = cmd[0:l-2]
            opcode = int(opStr)
            self.pmodes = list(map(lambda x: int(x), pmodesStr))
            self.pmodes.reverse()

        if opcode == 99:
            self.end = True
            return

        self.end = False        
        self.op = ops[opcode - 1]
        while len(self.pmodes) < self.op.nval - 1:
            self.pmodes.append(0)

class Operation:
    def __init__(self, run, nval, name):
        self.run = run
        self.nval = nval
        self.name = name

def addOp(src, i, pmodes):
    p1 = int(src[i + 1])
    p2 = int(src[i + 2])
    p3 = int(src[i + 3])
    x = p1 if pmodes[0] == 1 else int(src[p1]) 
    y = p2 if pmodes[1] == 1 else int(src[p2])
    src[p3] = str(x + y)
    return Result(0, i + 4)

def multiplyOp(src, i, pmodes):
    p1 = int(src[i + 1])
    p2 = int(src[i + 2])
    p3 = int(src[i + 3])
    x = p1 if pmodes[0] == 1 else int(src[p1]) 
    y = p2 if pmodes[1] == 1 else int(src[p2])
    src[p3] = str(x * y)
    return Result(0, i + 4)

def inputOp(src, i, pmodes):
    p1 = int(src[i + 1])
    print('Enter system id:')
    src[p1] = input()
    return Result(0, i + 2)

def outputOp(src, i, pmodes):
    p1 = int(src[i + 1])
    return Result(int(src[p1]), i + 2)

def jumpTrueOp(src, i, pmodes):
    p1 = int(src[i + 1])
    p2 = int(src[i + 2])
    x = p1 if pmodes[0] == 1 else int(src[p1]) 
    y = p2 if pmodes[1] == 1 else int(src[p2])
    return Result(0, y if x != 0 else i + 3)

def jumpFalseOp(src, i, pmodes):
    p1 = int(src[i + 1])
    p2 = int(src[i + 2])
    x = p1 if pmodes[0] == 1 else int(src[p1])
    y = p2 if pmodes[1] == 1 else int(src[p2])
    return Result(0, y if x == 0 else i + 3)

def lessThanOp(src, i, pmodes):
    p1 = int(src[i + 1])
    p2 = int(src[i + 2])
    p3 = int(src[i + 3])
    x = p1 if pmodes[0] == 1 else int(src[p1]) 
    y = p2 if pmodes[1] == 1 else int(src[p2])
    src[p3] = 1 if x < y else 0
    return Result(0, i + 4)

def equalsOp(src, i, pmodes):
    p1 = int(src[i + 1])
    p2 = int(src[i + 2])
    p3 = int(src[i + 3])
    x = p1 if pmodes[0] == 1 else int(src[p1]) 
    y = p2 if pmodes[1] == 1 else int(src[p2])
    src[p3] = 1 if x == y else 0
    return Result(0, i + 4)

ops = [
    Operation(addOp, 4, 'add'),
    Operation(multiplyOp, 4, 'multiply'),
    Operation(inputOp, 2, 'input'),
    Operation(outputOp, 2, 'output'),
    Operation(jumpTrueOp, 3, "jump-if-true"),
    Operation(jumpFalseOp, 3, "jump-if-false"),
    Operation(lessThanOp, 4, "less than"),
    Operation(equalsOp, 4, "equals")
]

def run(args):
    values = args[0].split(',')
    i = 0
    while i < len(values):
        val = values[i]
        c = Command(values, i)
        if c.end: return

        print(f'Parsing command at i=={i} ({val}): {c.op.name}')
        result = c.op.run(values, i, c.pmodes)
        if result.error != 0: print(f'ERR {result.error} found at command i=={i}')

        i = result.nexti
    