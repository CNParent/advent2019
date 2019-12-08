def matchingDigits(val):
    strval = str(val)
    i = 0
    while i < len(strval) - 1:
        if strval[i] == strval[i + 1]: return True
        i += 1

    return False

def doesNotDecrease(val):
    strval = str(val)
    i = 0
    while i < len(strval) - 1:
        if int(strval[i]) > int(strval[i+1]): return False
        i += 1

    return True 

def passwordCheck(val):
    return (matchingDigits(val) and doesNotDecrease(val))

def run(args):
    values = args[0].split('-')
    current = int(values[0])
    maxval = int(values[1])
    found = []
    while current <= maxval:
        if passwordCheck(current): found.append(current)
        current += 1

    return len(found)