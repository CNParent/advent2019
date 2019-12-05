operations = [
    lambda x,y: x + y,
    lambda x,y: x * y
]

class Replace:
    def __init__(self, index, value):
        self.index = index
        self.value = value

def process(values, replace = []):
    for r in replace:
        values[r.index] = r.value

    position = 0
    while True:
        op = values[position]
        if op > len(operations): return values

        x = values[position + 1]
        y = values[position + 2]
        storeat = values[position + 3]
        result = operations[op - 1](values[x], values[y])
        values[storeat] = result
        print(f'values[{storeat}] = {result}')
        position += 4

def run(args):
    noun = 0
    verb = 0
    while True:
        values = list(map(lambda x: int(x), args[0].split(',')))
        result = process(values, [Replace(1, noun), Replace(2, verb)])
        if result[0] == 19690720: return 100 * noun + verb
        
        noun += 1
        if noun > 99:
            noun = 0
            verb += 1
