from tools import sum

sq = 0
for i in range(1,101):
	sq += i**2
	
print(sum(0,100)**2 - sq)