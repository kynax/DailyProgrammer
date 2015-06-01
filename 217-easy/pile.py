def printPiles(p,n):
	for i in range(n):
		print(' '.join(map(str, p[i*n:(i+1)*n])))
		
	
size = int(input())
logs = int(input())
piles = []

for i in range(size):
	t = input().split()
	for c in t:
		piles.append(int(c))

idx = 0
while logs > 0:
	smallest = min(piles)
	sIdx = piles.index(smallest)
	for i in range(sIdx, len(piles)):
		if piles[i] == smallest:
			piles[i] = smallest + 1
			logs = logs - 1
			if logs == 0:
				break
	
printPiles(piles, size)