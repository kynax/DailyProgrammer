from tools import ispalindrome

best = 0

for a in range(999, 100, -1):
	for b in range(999,100,-1):
	
		if ispalindrome(a*b):
			if a*b > best:
				best = a*b

print(best)