import t06p1

test = [1,2,3]
print(list(filter(lambda x: x > 2, test)))

args = [
	'COM)B',
	'B)C',
	'C)D',
	'D)E',
	'E)F',
	'B)G',
	'G)H',
	'D)I',
	'E)J',
	'J)K',
	'K)L'
]
print(t06p1.run(args))