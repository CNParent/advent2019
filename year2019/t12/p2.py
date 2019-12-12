import sys
import time

class Point:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z
		
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def getMagnitude(self):
		return abs(self.x) + abs(self.y) + abs(self.z)

class Body:
	def __init__(self, pos, vel):
		self.pos = pos
		self.vel = vel

	def __eq__(self, other):
		return self.pos == other.pos
		
	def gravitate(self, other):
		dx = other.pos.x - self.pos.x
		dy = other.pos.y - self.pos.y
		dz = other.pos.z - self.pos.z
		if dx != 0: dx = dx / abs(dx)
		if dy != 0: dy = dy / abs(dy)
		if dz != 0: dz = dz / abs(dz)
		
		self.vel.x += dx
		self.vel.y += dy
		self.vel.z += dz
		
	def move(self):
		self.pos.x += self.vel.x
		self.pos.y += self.vel.y
		self.pos.z += self.vel.z
		
	def getEnergy(self):
		return self.pos.getMagnitude() * self.vel.getMagnitude()

class System:
	def __init__(self, bodies):
		self.bodies = bodies

	def __eq__(self, other):
		return all(self.bodies[i] == other.bodies[i] for i in range(0, len(self.bodies)))
		
	def step(self):
		for i in range(0, len(self.bodies)):
			for j in range(0, len(self.bodies)):
				self.bodies[i].gravitate(self.bodies[j])
				
		for b in self.bodies: b.move()
		
	def getEnergy(self):
		return sum(b.getEnergy() for b in self.bodies)

	def equals(self, other):
		n = len(self.bodies)
		if any(self.bodies[i] != other.bodies[i] for i in range(0, n)): return False
		else: return all(self.bodies[i] == other.bodies[i] for i in range(0, n))
		
def parseBody(text):
	text = text.replace('>', '').replace('<', '').replace(' ','')
	pointsTxt = text.split(',')
	x = float(pointsTxt[0].split('=')[1])
	y = float(pointsTxt[1].split('=')[1])
	z = float(pointsTxt[2].split('=')[1])
	return Body(Point(x, y, z), Point(0, 0, 0))

def run(args):
	o = System(list(parseBody(text) for text in args))
	s = System(list(parseBody(text) for text in args))
	n = 0
	ts = time.time()
	while True:
		n += 1
		s.step()
		if s == o: return n
		if n > 1000000: return f'Process took {time.time() - ts} to reach 1 000 000 iterations'
		if n % 10000 == 0: print(f'{n} of {4686774924}', end='\r', flush=True)
