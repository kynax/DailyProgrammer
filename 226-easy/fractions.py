def reduce(num, den):
	n = num
	d = den
	for i in range(num, 1, -1):
		if n % i == 0 and d % i == 0:
			n /= i
			d /= i
	
	return int(n),int(d)
	
def add(n1, d1, n2, d2):
	n = n1 * d2 + n2 * d1
	d = d1 * d2
	return reduce(n,d)
	
count = int(input())
cn = 0
cd = 1
for i in range(count):
	n,d = input().split('/')
	cn,cd = add(cn,cd,int(n),int(d))
	#print("{} : {}/{}".format(i,cn,cd))
	
print("{}/{}".format(cn,cd))