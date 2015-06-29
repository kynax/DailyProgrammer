a = 1
b = 2
next = 3
sum = 2

while next <= 4000000:
	next = a + b
	if next % 2 == 0:
		sum += next
	a = b
	b = next
	
print(sum)