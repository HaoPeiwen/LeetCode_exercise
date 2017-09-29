def merge(list,n):
	new_list = []
	index = [0]*n
	total_number = 0
	for i in list:
		total_number += len(i)
	while total_number>len(new_list):
		small = 1000
		small_index = 0
		for i in range(len(list)):
			if index[i]<len(list[i]) and list[i][index[i]]<small :
				small = list[i][index[i]]
				small_index = i
		new_list.append(small)
		index[small_index] += 1
	return new_list

list1 = [1,4,6,8,12,100]
list2 = [3,5,23,66,101,102,103]
list3 = [2,4,6,99,109,123,300]
list = [list1,list2,list3]
n = 3
print merge(list,n)

