def sm(max):
	for n in range(2*3*5*7*11*13*17, max, 2*3*5*7*11*13*17):
		good = True
		for i in range(2,20):
			if n % i != 0:
				good = False
				break
		
		if good:
			return n
	return -1
	
print(sm(999999999999))