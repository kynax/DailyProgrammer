from random import randrange
from random import random

verbose = True

class Forest:
	"""A huge forest, full of trees, bears and lumberjacks."""
	
	def __init__(self, size):
		self.size = size
		self.things = [[' ' for col in range(self.size)] for row in range(self.size) ]
		self.age = 0
		self.lumber = 0
		self.newLumber = 0
		self.newTrees = 0
		self.killedLj = 0
		self.upgradedT = 0
		self.initialFill()
		self.summary()
		
	def initialFill(self):
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
		return self.things[x][y] == None or self.things[x][y] == ' '
		
	def emptySquare(self, x, y):
		self.things[x][y] = None
		
	def tick(self):
		# New month, things activate
		self.age += 1
		for t in things:
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
		print("[Month {}]".format(self.age))
		
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
		moves = speed
		while moves > 0:
			mx = randrange(-1, 2, 1)
			my = randrange(-1, 2, 1)
			if mx == 0 and my == 0:
				continue
			
			# move there
			# if action, stop moving
			moves -= 1
			
	def action(self):
		pass
	
	def tick(self):
		self.move(self.speed)
		self.action()
		
class Lumberjack(Thing):
	"""Lumberjack walking around the forest looking for suitable trees to cut down."""

	speed = 3
		
	#def action(self):
		# Cut down a tree if there is one
		
	def __str__(self):
		return "L"
		
		
class Bear(Thing):
	"""Bear strolling around the forest looking for delicious lumberjacks to chew."""

	speed = 5
		
	#def action(self):
		# Eat a lumberjack if there is one
		
	def __str__(self):
		return "B"
	
	
class Tree(Thing):
	"""Tree standing in place in the forest, spawning sapplings and getting old."""
	
	speed = 0 # Obviously!
	
	def __init__(self, x, y):
		self.age = 0 # Newly born!
		self.type = 0 # Sappling
		Thing.__init__(self, x, y)
	
	def action(self):
		# Spawn a tree!
		if random.random() < self.type * 0.1:
			# Yup, find an empty spot
			print("Spawning sappling at {},{}")
	
	def __str__(self):
		return str(self.type)
		
forest = Forest(20)
forest.print()