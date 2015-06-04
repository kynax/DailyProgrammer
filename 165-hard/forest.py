from random import randrange
from random import random
from random import choice

verbose = True

class Forest:
	"""A huge forest, full of trees, bears and lumberjacks."""
	
	_shared_state = {} # Borg pattern (singleton)
        
	def __init__(self, size):
		self.__dict__ = self._shared_state
		if "filled" in self._shared_state:
			return 
			
		self.size = size
		self.things = [[' ' for col in range(self.size)] for row in range(self.size) ]
		self.age = 0
		self.lumber = 0
		self.newLumber = 0
		self.newTrees = 0
		self.killedLj = 0
		self.upgradedT = 0
	
		self.initialFill()
		self.filled = True
		
	def initialFill(self):
		print("Filling a new forest.")
		nbLumberjacks = (self.size ** 2) * 0.1
		nbTrees = (self.size ** 2) * 0.5
		nbBears = (self.size ** 2) * 0.02
		
		while nbLumberjacks > 0:
			x, y = int(random() * self.size), int(random() * self.size)
			if not self.isEmpty(x, y):
				continue
			t = Lumberjack(x, y)
			self.things[x][y] = t
			nbLumberjacks -= 1
			
		while nbTrees > 0:
			x, y = int(random() * self.size), int(random() * self.size)
			if not self.isEmpty(x, y):
				continue
			t = Tree(x, y)
			self.things[x][y] = t
			nbTrees -= 1
			
		while nbBears > 0:
			x, y = int(random() * self.size), int(random() * self.size)
			if not self.isEmpty(x, y):
				continue
			t = Bear(x, y)
			self.things[x][y] = t
			nbBears -= 1
	
	def isEmpty(self, x, y):
		return self.things[x%self.size][y%self.size] == None or self.things[x%self.size][y%self.size] == ' '
		
	def emptySquare(self, x, y):
		self.things[x%self.size][y%self.size] = ' '
		
	def thing(self, x, y):
		return str(self.things[x%self.size][y%self.size])
		
	def setThing(self, x, y, t):
		self.things[x%self.size][y%self.size] = t
		if isinstance(t, Tree):
			self.newTrees += 1
		
	def tick(self):
		# New month, things activate
		self.age += 1
		for r in self.things:
			for t in r:
				if isinstance(t,Thing):
					t.tick()
		
		# End of the year, add/remove things
		#if self.age % 12 == 0:
			
		
		# Print everything
		if verbose:
			self.summary()
		
		self.newLumber = 0
		self.newTrees = 0
		self.killedLj = 0
		self.upgradedT = 0
			
	def summary(self):
		# Print monthly feedback
		if self.newTrees != 0:
			print("[Month {}] New trees : {}".format(self.age, self.newTrees))
		
		# Print end of year summary
		if self.age % 12 == 0:
			print("<Year {}>".format(self.age % 12))
			
	def print(self):
		for i in range(len(self.things)):
			print(*(self.things[i]))

class Thing:
	"""Something in the forest. What is it?"""
	speed = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def move(self):
		moves = self.speed
		worked = False
		while moves > 0 and not worked:
			mx = randrange(-1, 2, 1)
			my = randrange(-1, 2, 1)
			if mx == 0 and my == 0:
				continue
			mx = self.x + mx
			my = self.y + my
			thing = Forest(0).thing(mx, my)
			if self.movable(thing):
				if self.action(thing, mx, my):
					worked = True
			self.x = mx
			self.y = my
				
			moves -= 1
			
	def action(self, t, x, y):
		pass
	
	def movable(self, other):
		pass
	
	def tick(self):
		self.move()
		self.action(self, self.x, self.y)
		
class Lumberjack(Thing):
	"""Lumberjack walking around the forest looking for suitable trees to cut down."""

	speed = 3
		
	def action(self, thing, x, y):
		pass
		# Cut down a tree if there is one
	
	def movable(self, other):
		return other != 'B' and other != 'L'
		
	def __str__(self):
		return "L"
		
		
class Bear(Thing):
	"""Bear strolling around the forest looking for delicious lumberjacks to chew."""

	speed = 5
		
	def action(self, thing, x, y):
		pass
		# Eat a lumberjack if there is one
	
	def movable(self, other):
		return other != 'B'
	
	def __str__(self):
		return "B"
	
	
class Tree(Thing):
	"""Tree standing in place in the forest, spawning sapplings and getting old."""
	
	speed = 0 # Obviously!
	
	def __init__(self, x, y):
		self.age = 0 # Newly born!
		self.type = 0 # Sappling
		Thing.__init__(self, x, y)
	
	def action(self, thing, x, y):
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
					if Forest(0).isEmpty(mx,my):
						spots.append([mx, my])
			if len(spots) < 1:
				return
			
			newspot = choice(spots)
			t = Tree(newspot[0], newspot[1])
			Forest(0).setThing(newspot[0], newspot[1], t)
	
	def __str__(self):
		return str(self.type)
		
forest = Forest(20)
forest.print()

for i in range(125):
	print()
	print()
	forest.tick()
	forest.print()
