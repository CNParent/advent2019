import sys
import math

sys.path.append('')
sys.path.append('lib')

import lib.loadinput
import config
from stoichiometry import Nanofactory

args = lib.loadinput.get(14, 2019, config.sessionValue)
nf = Nanofactory(args)
nf.produce('FUEL')
print(nf.stores)
cap = 1000000000000
res = math.ceil(cap / abs(nf.stores['ORE']))
print(f'res: {res}')
while True:
    n = math.ceil(res * (cap - abs(nf.stores['ORE'])) / cap / 10)
    nf.produce('FUEL', n)
    if abs(nf.stores['ORE']) > cap: break

    print(f'FUEL: {nf.stores["FUEL"]} ORE: {abs(nf.stores["ORE"])}')

print()