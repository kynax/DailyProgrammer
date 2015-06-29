from tools import isprime
s = 0

for i in range(2000000):
	if isprime(i):
		s += i
		
print(s)