output = ""
consonents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

def enc(c):
	l = c.lower()
	if l in consonents:
		return c + 'o' + l
	return c

for c in input():
	output += enc(c)
	
print(output)