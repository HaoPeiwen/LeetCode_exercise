def com(list,target):
	# result1 matrix form
	result1 = []
	initial = [1]*len(list)
	index = traverse(initial)
	for item in index:
		sum = 0
		for j in range(len(item)):
			sum += item[j]*list[j]
		if sum==target :
			result1.append(item)

	#result2 solve form
	result2 = []
	for item in result1:
		temp = []
		for j in range(len(item)):
			for i in range(item[j]):
				temp.append(list[j])
		temp = sorted(temp)
		if temp not in result2 :
			result2.append(temp)
	return result2

def traverse(list):
	if len(list)==0 :
		return [[]]
	sum = []
	for i in range(list[0]+1):
		for item in traverse(list[1:]):
			sum.append([i]+item)
	return sum

list = [10, 1, 2, 7, 6, 1, 5]
target = 8
print com(list,target)