# get all concatenation
def getCon(list):
	traverse = []
	if len(list)==1 :
		return [list] 
	else :
		for i in range(len(list)):
			list[0],list[i] = list[i],list[0]
			temp = getCon(list[1:])
			for j in temp:
				traverse.append([list[0]]+j)
	return traverse

# change list to string
def getString(list):
	temp = []
	for i in list:
		temp.append(''.join(i))
	return temp

# bruce force
def judge(s,list):
	indices = []
	length = len(list[0])
	for i in range(len(s)-length):
		temp = s[i:i+length]
		for j in list:
			if temp==j :
				indices.append(i)
				break
	return indices
s = "zyrycqngownguenviornfiowfoafjkajfkljfkycqzyr\
ajnfjasnjfndsajfndsafndjsncdcdycqzyrweycqzyrajsdnv\
zyrycqajvoaksowordsjsdanafafdsfaafjdnfdnfzyraaycq"		
words = ["zyr", "ycq"]
print judge(s,getString(getCon(words)))
