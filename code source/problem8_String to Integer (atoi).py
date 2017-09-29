def str2int(string):
	# judge negative or whether
	negative = 0
	if string[0]=='-':
		negative = 1
		string = string[1:]
	# delete pre-zero
	k = 0
	while string[k]=='0':
		k += 1
	string = string[k:]
	# get integer
	sum = 0
	for i in range(len(string)):
		sum = sum*10+ord(string[i])-ord('0')
	return  sum*((-1)**negative)

string = '-012343'
print str2int(string)

