import t04p1

def check(text, value, expected):
    print(f'{text} == {expected}: value was {value}, {"PASS" if value == expected else "FAIL"}')

result = t04p1.matchingDigits('1234456')
check('Has match', result, True)

result = t04p1.matchingDigits('1234567')
check('Has no match', result, False)

result = t04p1.doesNotDecrease('1123456')
check('Does not decrease', result, True)

result = t04p1.doesNotDecrease('9876554')
check('Does not decrease', result, False)

args = ['12-23']
result = t04p1.run(args)
check('One match', result, 1)