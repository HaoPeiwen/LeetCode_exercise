def judge(string):
	# diff is '('-')'
	diff = 0
	index = 0
	while diff>=0 and index<len(string) :
		if string[index]=='(' :
			diff += 1
		else :
			diff -= 1
		if diff<0 :
			return -1
		index += 1
	return 1

def find_valid(string):
	max_length = 0
	for i in range(len(string)):
		for j in range(i):
			pass
			temp = string[j:i+1]
			if judge(temp)==1 and len(temp)>max_length :
				max_length = len(temp)
	return max_length

string="()()"
print find_valid(string)