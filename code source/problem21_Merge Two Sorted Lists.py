def merge(list1,list2):
	new_list=[]
	index1 = 0
	index2 = 0
	while len(list1)+len(list2)>len(new_list):
		if index1<len(list1) and index2<len(list2) and list1[index1]<list2[index2]:
			new_list.append(list1[index1])
			index1 += 1
		elif index1<len(list1) and index2<len(list2):
			new_list.append(list2[index2])
			index2 += 1
		elif index1<len(list1):
			new_list.append(list1[index1])
		else:
			new_list.append(list2[index2])
	return new_list
list1 = [1,4,6,8,12,100]
list2 = [3,5,23,66,457]
print merge(list1,list2)