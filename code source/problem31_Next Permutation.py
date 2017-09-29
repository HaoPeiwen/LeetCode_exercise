def next_permutation(list):
	# find the chang position 6,9
	for i in range(2,len(list)+1,1):
		if list[-i]<list[-i+1] :
			break
	for j in range(1,i,1) :
		if list[-j]>list[-i] :
			break
	if i<len(list) :
		list[-i],list[-j] = list[-j],list[-i]
		#print i,j,list
		# change the number and reverse the numbers after 9
		for j in range(1,i/2+1,1) :
			list[-j],list[j-i] = list[j-i],list[-j]
		return list
	else :
		for j in range(len(list)/2) :
			list[j],list[len(list)-1-j] = list[len(list)-1-j],list[j]
		return list

#list = [5,4,3,2,1]
list = [6,7,9,8,5,4,2,1]
print next_permutation(list)