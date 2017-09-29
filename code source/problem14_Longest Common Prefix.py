def common_prefix(string):
	process = zip(*string)
	prefix = ''
	for i in process:
		k = 0
		temp = i[0]
		for j in i :
			if j!=temp :
				k=1
		if k==0 :
			prefix+=temp
		else :
			break
	return prefix

string = ["abcdefg","abcfs","abciueo"]
print common_prefix(string)