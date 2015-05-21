#Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

list = [1, 3, 5, 2, 9, 10]

def addFor():
	total = 0
	for i in list:
		total += i
	return total

def addWhile():
	idx = 0
	total = 0
	while idx < len(list):
		total += list[idx]
		idx += 1
	return total

def recurse(l):
	if len(l) == 1:
		return l[0]
	return l[0] + recurse(l[1:])
	
def addRecursive():
	return recurse(list)
	
print(addFor());
print(addWhile());
print(addRecursive());