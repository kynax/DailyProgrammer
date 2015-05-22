config = input().split(" ")
nbWires = int(config[0])
nbComps = int(config[1])
network = []

def readNetwork():
	for i in range(nbComps):
		inp = input().split(" ")
		network.append( [int(inp[0]), int(inp[1])] )

def run(i):
	for c in network:
		a = i[c[0]]
		b = i[c[1]]
		if a > b:
			i[c[0]] = b 
			i[c[1]] = a
	return i

def isSorted(c):
	for i in range(len(c)-1):
		if c[i] > c[i+1]:
			return False
	return True

def tests():
	for i in range(nbWires ** 2):
		b = bin(i)[2:].zfill(nbWires)
		l = [int(x) for x in b]
		yield l

def validate():
	test = tests()
	valid = True
	for t in test:
		if not isSorted(run(t)):
			valid = False
			break
			
	if valid:
		print("Valid")
	else:
		print("Not valid")
		
readNetwork()
validate()
