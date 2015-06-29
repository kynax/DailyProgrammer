from tools import isPrime

number = 600851475143
max = int(number ** 0.5)
best = 0

for i in range(max, 1, -1):
	if number % i == 0:
		if isPrime(i):
			best = i
			break

print(best)