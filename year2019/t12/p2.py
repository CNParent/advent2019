import math
from itertools import product

def parseBody(text):
	text = text.replace('>', '').replace('<', '').replace(' ','')
	pointsTxt = text.split(',')
	x = int(pointsTxt[0].split('=')[1])
	y = int(pointsTxt[1].split('=')[1])
	z = int(pointsTxt[2].split('=')[1])
	return [x, y, z, 0, 0, 0]

def delta(a, b):
	if a == b: return 0
	elif a < b: return 1
	else: return -1

def getCount(o, s, i):
	count = 0
	while True:
		count += 1
		for a, b in product(s, s): a[i + 3] += delta(a[i], b[i])
		for a in s: a[i] += a[i + 3]
		if all(o[n][i] == s[n][i] and o[n][i + 3] == s[n][i + 3] for n in range(0, len(o))): return count

def run(args):
	o = list(parseBody(text) for text in args)
	s = list(parseBody(text) for text in args)
	t = []
	for i in range(0,3): 
		t.append(getCount(o, s, i))

	while len(t) > 1:
		t[0] = int(t[0] * t[1] / math.gcd(t[0], t[1]))
		t.remove(t[1])

	return t[0]