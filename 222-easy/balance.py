alpha = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def isBalanced(word, n):
	vl = 0
	vr = 0
	for i in range(n):
		vl += alpha.index(word[i]) * (n-i)
		
	for i in range(n+1, len(word)):
		vr += alpha.index(word[i]) * (i-n)
	
	return (vl == vr), vl
			
def balance(word):
	for i in range(len(word)):
		b,w = isBalanced(word,i)
		if b:
			print(word[0:i],word[i],word[i+1:],"-",w)
			return
	print(word, "DOES NOT BALANCE")

balance(input())