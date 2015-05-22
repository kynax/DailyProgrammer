A = 'a'
B = 'b'
def discrepancy(s):
	return abs(s.count(A) - s.count(B))

max = -1
ms = ""

#while True:
str = input()
#if str == "":
#	break
	
l = len(str)

for i in range(l):
	for j in range(l+1):
		for s in range(1,l):
			d = discrepancy(str[i:j:s])
			if d > max:
				max = d
				ms = "s[{0}:{1}:{2}]".format(i,j,s)
				
print(max)
#print(ms)