import math

class Reaction:
    def __init__(self, expression):
        sides = expression.split(' => ')
        (ls, rs) = (sides[0].split(', '), sides[1])
        self.ins = dict()
        for x in ls:
            v = x.split(' ')
            self.ins[v[1]] = int(v[0])

        v = rs.split(' ')
        self.out = v[1]
        self.count = int(v[0])

    def produceWith(self, stores, n):
        n = math.ceil(n / self.count)
        for k in self.ins:
            stores[k] -= self.ins[k] * n

        stores[self.out] += self.count * n

class Nanofactory:
    def __init__(self, args):
        self.reactions = dict()
        self.stores = dict()
        self.stores['ORE'] = 0
        for r in list(Reaction(a) for a in args): 
            self.reactions[r.out] = r
            self.stores[r.out] = 0 

    def produce(self, name, n = 1):
        rxn = self.reactions[name]
        rxn.produceWith(self.stores, n)
        for k in rxn.ins:
            if k == 'ORE': continue
            while self.stores[k] < 0: self.produce(k, n)
