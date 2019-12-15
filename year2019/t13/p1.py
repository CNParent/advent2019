import sys
import time
sys.path.append('')
sys.path.append('lib')

import lib.intcode
import loadinput
import config

gameobjects = [
    ' ',
    '+',
    '#',
    '=',
    'o'
]

def printTiles(tiles):
    xvals = list(map(lambda k: int(k.split(',')[0]), tiles))
    yvals = list(map(lambda k: int(k.split(',')[1]), tiles))
    minx = min(xvals)
    maxx = max(xvals) + 1
    miny = min(yvals)
    maxy = max(yvals) + 1

    for i in range(miny, maxy):
        for j in range(minx, maxx):
            key = f'{j},{i}'
            yield gameobjects[tiles[key]]
        yield '\n'

args = loadinput.get(13, 2019, config.sessionValue)
values = list(int(x) for x in args[0].split(','))
p = lib.intcode.Program(values)
p.run()

tiles = dict()
for i in range(0, int(len(p.outputs) / 3)):
    key = f'{p.outputs[i * 3]},{p.outputs[i * 3 + 1]}'
    tiles[key] = p.outputs[i * 3 + 2]

print(p.end)
nblocks = 0
for key in tiles:
    if tiles[key] == 2: nblocks += 1

print(f'There are {nblocks} blocks when the game exits')

values = list(int(x) for x in args[0].split(','))
values[0] = 2
p = lib.intcode.Program(values)

tiles = dict()
score = 0
padx = 0
ballx = 0
while not p.end:
    p.run()

    for i in range(0, int(len(p.outputs) / 3)):
        v = p.outputs[i * 3:i * 3 + 3]
        if v[0] == -1 and v[1] == 0: score = v[2]
        else:
            key = f'{v[0]},{v[1]}'
            tiles[key] = v[2]

        if v[2] == 3: padx = v[0]
        elif v[2] == 4: ballx = v[0]

    print(f'Score: {score}', end='\r', flush=True)
    if padx < ballx: p.inputs = [1]
    elif padx > ballx: p.inputs = [-1]
    else: p.inputs = [0]

print(p.end)