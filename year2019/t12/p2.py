class Point:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z
		
	def getMagnitude(self):
		return abs(self.x) + abs(self.y) + abs(self.z)

	def fastHash(self):
		return self.x * 10000 + self.y * 100 + self.z

	def slowHash(self):
		return f'{self.x}{self.y}{self.z}'

class Body:
	def __init__(self, pos, vel):
		self.pos = pos
		self.vel = vel
		
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

	def fastHash(self):
		return self.pos.fastHash() * 10000 + self.vel.fastHash()

	def slowHash(self):
		return f'{self.pos.slowHash()}{self.vel.slowHash()}'

class System:
	def __init__(self, bodies):
		self.bodies = bodies
		
	def step(self):
		for i in range(0, len(self.bodies)):
			for j in range(0, len(self.bodies)):
				self.bodies[i].gravitate(self.bodies[j])
				
		for b in self.bodies: b.move()
		
	def getEnergy(self):
		return sum(b.getEnergy() for b in self.bodies)

	def fastHash(self):
		return sum(b.fastHash() for b in self.bodies)

	def slowHash(self):
		return ''.join(b.slowHash() for b in self.bodies)
		
def parseBody(text):
	text = text.replace('>', '').replace('<', '').replace(' ','')
	pointsTxt = text.split(',')
	x = int(pointsTxt[0].split('=')[1])
	y = int(pointsTxt[1].split('=')[1])
	z = int(pointsTxt[2].split('=')[1])
	return Body(Point(x, y, z), Point(0, 0, 0))
	
def run(args):
	bodies = list(parseBody(text) for text in args)	
	s = System(bodies)
	fast = set()
	slow = set()
	while True:
		if s.fastHash() in fast and s.slowHash in slow: return len(cfg)
		if len(fast) > 4686774924: return 'Error'
		if len(fast) % 10000 == 0: print(f'Attempt {len(cfg)}')

		fast.add(s.fastHash())
		slow.add(s.slowHash())
		s.step()