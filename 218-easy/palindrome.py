start = -1
steps = 0
val = 0

def isPalindrome(n):
	for a,b in zip(str(n),str(n)[::-1]):
		if a != b:
			return False
	return True

start = int(input())
val = start
steps = 0
while True:
	if isPalindrome(val):
		break

	steps += 1
	r = int(str(val)[::-1])
	val = val+r
	
print("{} gets palindromic after {} steps: {}".format(start, steps, val))
