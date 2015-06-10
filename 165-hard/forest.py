from random import randrange
from random import random
from random import choice

from colorama import init
from colorama import Fore, Back, Style
init()

verbose = False
graphics = True

class Forest:
	"""A huge forest, full of trees, bears and lumberjacks."""
	
	_shared_state = {} # Borg pattern (singleton)
        
	def __init__(self, size):
		self.__dict__ = self._shared_state
		if "filled" in self._shared_state:
			return 
			
		self.size = size
		self.things = [[None for col in range(self.size)] for row in range(self.size) ]
		self.ground = [[None for col in range(self.size)] for row in range(self.size) ]
		self.age = 0
		self.lumber = 0
		self.newLumber = 0
		self.newTrees = 0
		self.killedLj = 0
		self.upgradedT = 0
			
		self.initialFill()
		self.filled = True
		self.clearConsole()
		self.summary()
		
		
	def initialFill(self):
		print("Filling a new forest.")
		nbLumberjacks = (self.size ** 2) * 0.1
		nbTrees = (self.size ** 2) * 0.5
		nbBears = (self.size ** 2) * 0.02
		
		while nbLumberjacks > 0:
			self.addLumberjack()
			nbLumberjacks -= 1
			
		while nbTrees > 0:
			x, y = int(random() * self.size), int(random() * self.size)
			if not self.isEmptyGround(x, y):
				continue
			t = Tree(x, y)
			t.type = 1
			self.ground[x][y] = t
			nbTrees -= 1
			
		while nbBears > 0:
			self.addBear()
			nbBears -= 1
	
	def addLumberjack(self):
		while True:
			x, y = int(random() * self.size), int(random() * self.size)
			if not self.isEmpty(x, y):
				continue
			t = Lumberjack(x, y)
			self.things[x][y] = t
			return
	
	def removeLumberjack(self):
		while True:
			x = randrange(self.size)
			y = randrange(self.size)
			if isinstance(self.thingAt(x,y), Lumberjack):
				self.removeThing(x,y)
				return
				
	def addBear(self):
		while True:
			x, y = int(random() * self.size), int(random() * self.size)
			if not self.isEmpty(x, y):
				continue
			t = Bear(x, y)
			self.things[x][y] = t
			return
	
	def removeBear(self):
		while True:
			x = randrange(self.size)
			y = randrange(self.size)
			if isinstance(self.thingAt(x,y), Bear):
				self.removeThing(x,y)
				return

			
	def isEmpty(self, x, y):
		return self.things[x%self.size][y%self.size] == None

	def isEmptyGround(self, x, y):
		return self.ground[x%self.size][y%self.size] == None
		
	def removeThing(self, x, y):
		self.things[x%self.size][y%self.size] = None

	def removeGround(self, x, y):
		self.ground[x%self.size][y%self.size] = None
		
	def thingAt(self, x, y):
		return self.things[x%self.size][y%self.size]
		
	def groundAt(self, x, y):
		return self.ground[x%self.size][y%self.size]
		
	def setThing(self, x, y, t):
		if not self.isEmpty(x,y):
			raise ValueError("There is already something at {},{} : {}".format(x,y,self.thingAt(x,y)))
		self.things[x%self.size][y%self.size] = t
	
	def setGround(self, x, y, t):
		self.ground[x%self.size][y%self.size] = t
		if isinstance(t, Tree):
			self.newTrees += 1
		
	def tick(self):
		# New month, things activate
		self.age += 1
		
		for r in self.ground:
			for t in r:
				if isinstance(t,Thing):
					t.tick()
					
		for r in self.things:
			for t in r:
				if isinstance(t,Thing):
					t.tick()
		
		# End of the year, add/remove things
		if self.age % 12 == 0:
			lj, bears, t0,t1,t2 = self.count()
			
			# Add lumberjacks
			if self.newLumber > lj:
				nbHires = int(self.newLumber - lj) / 10
				while nbHires > 0:
					self.addLumberjack()
					nbHires -= 1
			if self.newLumber < lj:
				self.removeLumberjack()
			
			# Zoo keeper
			if self.killedLj > 0:
				self.removeBear()
			if self.killedLj == 0:
				self.addBear()
			# Clear counts for next year
			self.newLumber = 0
			self.killedLj = 0
		
		# Print everything
		if verbose:
			self.summary()
		if graphics:
			self.print()
		
		self.newTrees = 0
		self.upgradedT = 0
			
	def count(self):
		lj = 0
		bears = 0
		t0 = 0
		t1 = 0
		t2 = 0
		
		for x in range(self.size):
			for y in range(self.size):
				t = self.thingAt(x,y) 
				if isinstance(t, Bear):
					bears += 1
				if isinstance(t, Lumberjack):
					lj += 1
				t = self.groundAt(x,y)
				if t != None:
					t = t.type
					if t == 0:
						t0 += 1
					if t == 1:
						t1 += 1
					if t == 2:
						t2 += 1
			
		return lj, bears, t0, t1, t2
		
	def summary(self):
		# Print monthly feedback
		print("[Month {}] ".format(self.age))
		if self.newTrees != 0:
			print("\tNew trees : {}".format(self.newTrees))
		if self.killedLj != 0:
			print("\tKilled LJ : {}".format(self.killedLj))
		if self.newLumber != 0:
			print("\tCut trees : {}".format(self.newLumber))

		
		# Print end of year summary
		if self.age % 12 == 0:
			print("<Year {}>".format(int(self.age / 12)))
			lj, bears, t0, t1, t2 = self.count()
			print("\tLumberjacks : {}\n\r\tBears : {}\n\r\tSapplings: {}\n\r\tTrees: {}\n\r\tElder trees : {}".format(lj, bears, t0, t1, t2))
			
			
	def print(self):
		lines = ""
		# Print the top line of the grid
		lines += "Month {}\n".format(self.age)
		gap = len(str(10))-1
		line = ""
		for i in range(gap):
			line += " "
		line += '|'
		for i in range(self.size):
			line += str(int(i % 10))
		lines += line+"\n"
		line = ""
		for i in range(self.size + gap + 1):
			line += '-'
		lines += line+"\n"
		
		for x in range(self.size):
			line = Style.RESET_ALL + str(int(x % 10)) + '|'
			for y in range(self.size):
			
				t = self.thingAt(x, y)
				g = self.groundAt(x,y)
				
				if g != None:
					if g.type == 0:
						line += Back.YELLOW
					if g.type == 1:
						line += Back.GREEN
					if g.type == 2:
						line += Back.CYAN
						
				if isinstance(t, Lumberjack):
					if t.age == 0:
						line += Style.BRIGHT
					line += Fore.BLUE + str(t)
					line += Style.NORMAL
				elif isinstance(t, Bear):
					if t.age == 0:
						line += Style.BRIGHT
					line += Fore.RED + str(t)
					line += Style.NORMAL
				else:
					line += ' '
				
				line += Style.RESET_ALL
				
			lines += line+"\n"
		pos = lambda y, x: '\x1b[%d;%dH' % (y, x)
		print(pos(1,1))
		print(lines)
				
	def clearConsole(self):
		for i in range(80):
			print()

class Thing:
	"""Something in the forest. What is it?"""
	speed = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.actions = 0
		self.age = 0
		
	def move(self):
		moves = self.speed
		worked = False
		iter = 0
		while moves > 0 and not worked:
			iter += 1

			mx = randrange(-1, 2, 1)
			my = randrange(-1, 2, 1)
			
			if iter > 100:
				Forest(0).print()
				raise ValueError("Could not move {} at {},{} mx,my = {},{}".format(self, self.x, self.y, mx, my))
			if mx == 0 and my == 0:
				continue
			mx = self.x + mx
			my = self.y + my
			thing = Forest(0).thingAt(mx, my)
			if self.movable(thing):
				if self.action(mx, my):
					worked = True
			else:
				continue
			
			Forest(0).removeThing(self.x, self.y)
			Forest(0).setThing(mx, my, self)
			self.x = int(mx % Forest(0).size) 
			self.y = int(my % Forest(0).size)
				
			moves -= 1
			
	def action(self, x, y):
		pass
	
	def movable(self, other):
		pass
	
	def tick(self):
		self.age += 1
		# Try to do something right here, if not, start moving around
		if not self.action(self.x, self.y):
			self.move()
		
class Lumberjack(Thing):
	"""Lumberjack walking around the forest looking for suitable trees to cut down."""

	speed = 3
	
	def action(self, x, y):
		f = Forest(0)
		t = f.groundAt(x,y)
		if t == None:
			return False
		
		value = t.type
		if value == 0:
			return False # don't cut sapplings
		
		f.removeGround(x,y)
		f.lumber += value
		f.newLumber += value
		
		self.actions += value
		
		return True
	
	def movable(self, other):
		return other == None # Lumberjacks can never share a square with another thing
		
	def __str__(self):
		return "L"
		
		
class Bear(Thing):
	"""Bear strolling around the forest looking for delicious lumberjacks to chew."""

	speed = 5
	
	def action(self, x, y):
		# Eat a lumberjack if there is one
		if isinstance(Forest(0).thingAt(x,y), Lumberjack):
			Forest(0).removeThing(x, y)
			Forest(0).killedLj += 1
			self.actions += 1

	
	def movable(self, other):
		return not isinstance(other, Bear)
	
	def __str__(self):
		return "B"
	
	
class Tree(Thing):
	"""Tree standing in place in the forest, spawning sapplings and getting old."""
	
	speed = 0 # Obviously!
	
	def __init__(self, x, y):
		self.type = 0 # Sappling
		Thing.__init__(self, x, y)
	
	def action(self, x, y):
		self.age += 1
		if self.age > 12:
			self.type = 1
		if self.age > 120:
			self.type = 2

		if self.type == 0:
			return 
			
		# Spawn a tree!
		if random() < self.type * 0.1:
			
			# Yup, find an empty spot
			spots = []
			for mx in range(x-1, x+2, 1):
				for my in range(y-1, y+2, 1):
					if Forest(0).isEmptyGround(mx,my):
						spots.append([mx, my])
			if len(spots) < 1:
				return
			
			newspot = choice(spots)
			t = Tree(newspot[0], newspot[1])
			Forest(0).setGround(newspot[0], newspot[1], t)
			self.actions += 1
	
	def __str__(self):
		return str(self.type)
		
forest = Forest(20)
forest.print()

for i in range(120):
	forest.tick()
