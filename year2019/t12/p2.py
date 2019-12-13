import time
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

def run(args):
	o = list(parseBody(text) for text in args)
	s = list(parseBody(text) for text in args)
	n = 0
	tgrav = 0
	tmove = 0
	tcomp = 0
	ts = time.time()
	while True:
		n += 1
		then = time.time()	
		for a, b, i in product(s, s, range(0, 3)):
			a[i + 3] += delta(a[i], b[i])
		tgrav += time.time() - then

		then = time.time()
		for a, i in product(s, range(0, 3)):
			a[i] += a[i + 3]
		tmove += time.time() - then

		then = time.time()
		if all(o[i][j] == s[i][j] for i, j in product(range(0, 4), range(0, 6))): return n
		if n > 1000000: return f'Process took {time.time() - ts} to reach 1 000 000 iterations. tgrav={tgrav} tmove={tmove} tcomp={tcomp}'
		if n % 1000 == 0: print(f'{n} of {4686774924}', end='\r', flush=True)
		tcomp += time.time() - then