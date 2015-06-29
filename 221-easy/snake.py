s = input()
first = True
spaces = 0
dir = "R"

for word in s.split():
	if first:
		print(word)
		spaces = len(word) - 1
		dir = "D"
		first = False
	
	if dir == "R":
		print("{}".format(word.rjust(spaces + len(word))))
		spaces += len(word)-1
		dir = "D"
	elif dir == "D":
		for c in word[1:len(word)-1]:
			print("{}".format(c.rjust(spaces+1)))
		dir = "R"

if dir == "R":
	print(word[len(word)-1].rjust(spaces+1))