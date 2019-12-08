import t04p2

def check(text, value, expected):
    print(f'{text} == {expected}: value was {value}, {"PASS" if value == expected else "FAIL"}')

result = t04p2.matchingDigits('1234456')
check('Has match', result, True)

result = t04p2.matchingDigits('1222567')
check('Has no match', result, False)

result = t04p2.doesNotDecrease('1123456')
check('Does not decrease', result, True)

result = t04p2.doesNotDecrease('9876554')
check('Does not decrease', result, False)

args = ['12-23']
result = t04p2.run(args)
check('One match', result, 1)