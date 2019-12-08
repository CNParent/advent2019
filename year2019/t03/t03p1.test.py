import t03p1

def check(text, value, expected):
    print(f'{text} == {expected}: value was {value}, {"PASS" if value == expected else "FAIL"}')

i1 = t03p1.instruction('U2')
check('i1.up', i1.up, True)
check('i1.down', i1.down, False)
check('i1.right', i1.right, False)
check('i1.left', i1.left, False)
check('i1.delta', i1.delta, 2)

a = t03p1.line(t03p1.point(3,0), t03p1.point(0,0))
check('a.minX()', a.minX(), 0)
check('a.maxX()', a.maxX(), 3)
check('a.minY()', a.minY(), 0)
check('a.maxY()', a.maxY(), 0)
check('a.minabsX()', a.minabsX(), 0)
check('a.minabsY()', a.minabsY(), 0)

b = t03p1.line(t03p1.point(1,4), t03p1.point(1,-2))
check('b.minX()', b.minX(), 1)
check('b.maxX()', b.maxX(), 1)
check('b.minY()', b.minY(), -2)
check('b.maxY()', b.maxY(), 4)
check('b.minabsX()', b.minabsX(), 1)
check('b.minabsY()', b.minabsY(), 2)

check('a.intersects(b)', a.intersects(b), True)

p = a.intersection(b)
check('p.x', p.x, 1)
check('p.y', p.y, 0)

args = ['R8,U5,L5,D3','U7,R6,D4,L4']
result = t03p1.run(args)
check('result', result, 6)

args = ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']
result = t03p1.run(args)
check('result', result, 159)

args= ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
result = t03p1.run(args)
check('result', result, 135)