def step(string):
	k = 0
	list = []
	while k<len(string):
		if k==len(string)-1 :
			if string[k]=='1' :
				list.append('11')
			else:
				list.append('12')
		elif string[k:k+2]=='11' :
			list.append('21')
			k += 1
		elif string[k]=='1' :
			list.append('11')
		else:
			list.append('12')
		k += 1
	return ''.join(list)

string='1'
times = 5
for i in range(times):
	string = step(string)
	print string
