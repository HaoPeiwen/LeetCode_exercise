def isMatch(Matched, Matcher):
	initial_length = len(Matcher)
	Matcher = Matcher.split('*')
	# k is number of *
	k = len(Matcher)-1
	# space means the number of generate from *
	space = len(Matched) - initial_length+2*k
	traverse_list = get_list(k,space)
	string_list=[]
	# fill with the traverse_list to get all the possible string
	for i in range(len(traverse_list)):
		string_temp=''
		for j in range(len(Matcher)-1):
			string_temp = string_temp+Matcher[j][:-1]+Matcher[j][-1]*traverse_list[i][j]
		string_temp = string_temp+Matcher[-1]
		string_list.append(string_temp)
	# match all the string with the Matched
	for i in range(len(string_list)):
		flag = 1
		for j in range(len(Matched)):
			if Matched[j]==string_list[i][j] or string_list[i][j]=='.' :
				pass
			else :
				flag = 0
				break
		if flag == 1 :
			return 'matched!'
	return 'not match!'

def get_list(k,space):
	list = []
	if k==1:
		return [[space]]
	elif space==0 :
		return [[0]*k]
	else:
		for i in range(space+1):
			temp = get_list(k-1,space-i)
			if len(temp)>1 :
				for j in range(len(temp)):
					list.append([i]+temp[j])
			else:
				list.append([i]+temp[0])
		return list

Matched = 'zhouyiran'
Matcher = 'z.*y.*r.*'
print isMatch(Matched,Matcher)