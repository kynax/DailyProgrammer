# Write a function that combines two lists by alternatingly taking elements. 
# For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

list1 = ["a", "b", "c" ]
list2 = [1, 2, 3, 4]

maxIdx = max(len(list1), len(list2))
list = []
for i in range(maxIdx):
	if i < len(list1):
		list.append(list1[i])
	if i < len(list2):
		list.append(list2[i])

print(list);