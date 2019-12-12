class Point:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z
		
	def getMagnitude(self):
		return abs(self.x) + abs(self.y) + abs(self.z)

class Body:
	def __init__(self, pos = Point(), vel = Point()):
		self.pos = pos
		self.vel = vel
		
	def gravitate(self, other):
		dx = self.pos.x - other.pos.x
		dy = self.pos.y - other.pos.y
		dz = self.pos.z - other.pos.z
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
		return self.pos.getMagnitude() + self.vel.getMagnitude()

class System:
	def __init__(self, bodies):
		self.bodies = bodies
		
	def step(self):
		for i in range(0, len(bodies)):
			for j in range(0, len(bodies)):
				self.bodies[i].gravitate(self.bodies[j])
				
		b.move() for b in self.bodies
		
	def getEnergy(self):
		return sum(b.getEnergy() for b in self.bodies)
		
def parseBody(text):
	pointsTxt = text.split(',')
	x = int(pointsTxt[0].split('=')[1])
	y = int(pointsTxt[1].split('=')[1])
	z = int(pointsTxt[2].split('=')[1])
	return Body(Point(x, y, z))
	
def partOne(args):
	bodies = list(parseBody(text) for text in args)	
	s = System(bodies)
	for i in range(0, 1000): s.step()
	
	return s
	
def run(args):
	result = partOne(args)
	return s.getEnergy()