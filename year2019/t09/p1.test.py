import p1

args = ['109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99']
vals = list(map(lambda x: int(x), args[0].split(',')))
results = p1.test(args)
print(results == vals)

args = ['1102,34915192,34915192,7,4,7,99,0']
vals = list(map(lambda x: int(x), args[0].split(',')))
print(len(str(p1.test(args)[0])) == 16)

args = ['104,1125899906842624,99']
vals = list(map(lambda x: int(x), args[0].split(',')))
results = p1.test(args)
print(results[0] == 1125899906842624)