def swap(list,k):
	for i in range(0,len(list)-k,k):
		# swap in group i with k items
		for j in range(k/2):
			t = list[i+k-1-j]
			list[i+k-1-j] = list[i+j]
			list[i+j] = t
	return list

def showList(list):
	for i in list:
		if list[-1]==i :
			print i
		else :
			print i,'->',


list = [2,4,6,99,109,123,300,1]
showList(list)
showList(swap(list,4))

