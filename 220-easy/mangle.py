from random import shuffle
s = input()
cur = ""
out = ""
cap = []

# Loop over all characters of the input string
for c in s:

	# If current char is not a letter, shuffle and add to output
	if not c.isalpha():
		cur = list(cur)
		shuffle(cur)
		
		# Output the letter with upper or lower depending on the position
		for i in range(len(cur)):
			if cap[i]:
				out += cur[i].upper()
			else:
				out += cur[i].lower()
		
		# Add separating char (not a letter)
		out += c
		
		# Reset current word and capital letter positions
		cur = ""
		cap = []
		continue
	
	# Here, current char is a letter so add it to current word 
	# and remember if its position is a capital letter
	cur += c
	cap.append(c.isupper())
		
	
print(out)