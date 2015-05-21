b = int(input())
n = int(input())
cycle = []
start = 0

def decompose(num):
	vals = [num % 10]
	while(num // 10 != 0):
		num = num // 10
		vals.append(num % 10)
		
	vals = vals[::-1]
	print("Decomposed into ", str(vals)[1:-1])
	return vals

	
def nextNum(n, b):
	num = 0
	for i in decompose(n):
		num = num + i ** b
		
	print(n, " transforms into ", num)
	return num	

for i in range(100):
	num = nextNum(n, b)
	if num in cycle:
		start = cycle.index(num)
		break
	cycle.append(num)
	n = num

print(cycle[start:])