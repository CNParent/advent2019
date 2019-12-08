class Program:
    def __init__(self, source = []):
        self.source = source
        self.inputs = []
        self.outputs = []
        self.end = False
        self.i = 0

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

    def setValueAt(self, n, value):
        i = self.getValue(n)
        self.source[i] = value

    def getValue(self, n):
        return self.source[self.i + n]

    def getValues(self, n):
        modes = self.getModes(n + 2)
        values = []
        m = 0
        while m < n:
            i = self.source[self.i + m + 1]
            if modes[m] == 1: values.append(i)
            else: values.append(self.source[i])
            m += 1

        return values

    def add(self):
        v = self.getValues(2)
        self.setValueAt(3, v[0] + v[1])
        self.move(4)

    def multiply(self):
        v = self.getValues(2)
        self.setValueAt(3, v[0] * v[1])
        self.move(4)

    def input(self):
        self.setValueAt(1, self.inputs.pop(0))
        self.move(2)

    def output(self):
        v = self.getValues(1)
        self.outputs.append(v[0])
        self.move(2)

    def jumpIfTrue(self):
        v = self.getValues(2)
        if v[0] != 0: self.i = v[1]
        else: self.move(3)

    def jumpIfFalse(self):
        v = self.getValues(2)
        if v[0] == 0: self.i = v[1]
        else: self.move(3)
        
    def lessThan(self):
        v = self.getValues(2)
        self.setValueAt(3, 1 if v[0] < v[1] else 0)
        self.move(4)
        
    def equals(self):
        v = self.getValues(2)
        self.setValueAt(3, 1 if v[0] == v[1] else 0)
        self.move(4)

class Amplifier:
    def __init__(self, values, size, settings):
        i = 0
        self.programs = []
        self.result = 0
        while i < size:
            self.programs.append(Program([] + values))
            self.programs[i].inputs.append(settings[i])
            i += 1

        self.programs[0].inputs.append(0)

    def isRunning(self):
        lastProgram = self.programs[len(self.programs) - 1]
        return not lastProgram.end 

    def run(self):
        outputs = []
        i = 0
        n = len(self.programs)
        while self.isRunning():
            program = self.programs[i%n]
            program.inputs.extend(outputs)
            program.run()
            outputs = program.outputs
            i += 1

        self.result = program.outputs[0]

def getConfigurations(settings):
    cfg = []
    if len(settings) == 2: return [[settings[0], settings[1]], [settings[1],settings[0]]]

    i = 0
    while i < len(settings):
        subsettings = [] + settings
        subsettings.remove(settings[i])
        for c in getConfigurations(subsettings):
            cfg.append([settings[i]] + c)
        i += 1

    return cfg

def run(args):
    values = list(map(lambda x: int(x), args[0].split(',')))
    configurations = getConfigurations([5,6,7,8,9])
    results = []
    for settings in configurations:
        amplifier = Amplifier([] + values, 5, settings)
        amplifier.run()
        results.append(amplifier.result)

    return max(results)