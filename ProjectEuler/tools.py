__list_of_primes = [2,3,5,7,9,11,13,17,19]

def isprime(n):

	currentBiggestPrime = max(__list_of_primes)
	
	# If sqrt(n) is small enough, it should be in the list
	if n**0.5 < currentBiggestPrime:
		for i in __list_of_primes:
			if n % i == 0:
				return False
		
		return True
	
	for i in range(currentBiggestPrime+1, int(n ** 0.5)):
		if isprime(i):
			__list_of_primes.append(i)

	return n in __list_of_primes

def ispalindrome(n):
	for a,b in zip(str(n),str(n)[::-1]):
		if a != b:
			return False
	return True

def sum(n,m):
	return int(m*(m+1)/2 - n*(n+1)/2)