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
    values = list(map(lambda x: int(x), args[0].split(',')))
    return process(values, [Replace(1,12), Replace(2,2)])
