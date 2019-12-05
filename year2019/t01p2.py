import math

def calculateFuel(mass):
    fuel = math.floor(int(mass)/3) - 2
    if fuel <= 0: return 0
    return fuel + calculateFuel(fuel)

def run(args):
    total = 0
    for x in args:
        total += calculateFuel(x)

    return total