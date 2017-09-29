def remove(list,index):
	if 1<index and index<len(list):
		return list[:len(list)-index]+list[len(list)-index+1:]
	elif index == 1:
		return list[1:]
	elif index == len(list) :
		return list[:-1]

def showList(list):
	for i in list:
		if list[-1]==i :
			print i
		else :
			print i,'->',

list = ['1','2','3','4','5']
showList(list)
showList(remove(list,1))