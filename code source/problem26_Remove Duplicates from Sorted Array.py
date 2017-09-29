def remove_duplicate(list):
	for i in range(len(list)):
		while i+1<len(list) and list[i] == list[i+1]:
			list = list[:i+1]+list[i+2:]
	return list

list = [1,1,1,2,2,3,5,5,4,4]
print remove_duplicate(list)
