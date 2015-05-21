# Write a function that computes the list of the first 100 Fibonacci numbers. 
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
# and each subsequent number is the sum of the previous two. As an example, 
# here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

p1 = 0
p2 = 1
print(p1)
print(p2)
for i in range(98):
	n = p1 + p2
	print(n)
	p1 = p2
	p2 = n
	