from string import Template
def problem(secret, offensive, output = True):
	word = ""
	for s in secret:
		if s in offensive:
			word += s
			
	if output:
		print("problem(""{}"", ""{}"") -> {}".format(secret, offensive, word == offensive))
	return word == offensive
		
problem("synchronized", "snond")
problem("misfunctioned", "snond")
problem("mispronounced", "snond")
problem("shotgunned", "snond")
problem("snond", "snond")

def score(offensive):
	score = 0
	for word in open("../enable1.txt"):
		if problem(word, offensive, False):
			score += 1
	return score
	
print()
print("Challenge: Find score of offensive word")
print("Offensive word snond has a score of " + str(score("snond")))
print("Offensive word rrizi has a score of " + str(score("rrizi")))
