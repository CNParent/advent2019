import t02p1

class TestCase:
    def __init__(self, valuein, valueout):
        self.valuein = valuein
        self.valueout = valueout

cases = [
    TestCase([1,0,0,0,99], [2,0,0,0,99]),
    TestCase([2,3,0,3,99], [2,3,0,6,99]),
    TestCase([2,4,4,5,99,0], [2,4,4,5,99,9801]),
    TestCase([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])
]

for case in cases:
    value = t02p1.process(case.valuein)
    print(f'in: {case.valuein}, out: {value}, pass: {value == case.valueout}\r\n')