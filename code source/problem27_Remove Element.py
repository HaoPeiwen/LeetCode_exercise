def remove(list,val):
	i = 0
	while i<len(list) :
		if  i<len(list) and list[i]==val:
			list = list[:i]+list[i+1:]
		else :
			i += 1
		if i>=len(list):
			break
	return list

list = [1,1,1,2,2,3,5,5,5,5,5,5,4,4]
val = 5
print remove(list,val)
