import math

def run(args):
    total = 0
    for x in args:
        total += math.floor((int(x))/3) - 2

    return total