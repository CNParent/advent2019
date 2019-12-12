import p1

args = [
    '<x=-1, y=0, z=2>',
    '<x=2, y=-10, z=-7>',
    '<x=4, y=-8, z=8>',
    '<x=3, y=5, z=-1>'
]

print(p1.partOne(args, 10).getEnergy() == 179)

args = [
    '<x=-8, y=-10, z=0>',  
    '<x=5, y=5, z=10>',
    '<x=2, y=-7, z=3>',
    '<x=9, y=-8, z=-3>'
]

print(p1.partOne(args, 100).getEnergy() == 1940)