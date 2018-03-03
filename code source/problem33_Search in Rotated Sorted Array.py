# find the start point of rotate
def find_start(list):
	for i in range(len(list)-1) :
		if list[i]>list[i+1] :
			return i+2
	return 1

# resort the list from 0
def resort(list,move):
	return list[move-1:]+list[:move-1]

# use bisearch to find the index
def find_index(list,start,end,target):
	if start>=end and target==list[start] :
		return start
	elif start>=end :
		return -1
	else :
		mid = (start+end)/2
	if list[mid]==target :
		return mid
	elif list[mid]>target :
		return find_index(list,start,mid-1,target)
	else :
		return find_index(list,mid+1,end,target)

list = [4,5,6,7,0,1,2,3]
#list = [1,2,3,4,5,6,7,0]
target = 2
# index= 8
move = find_start(list)
list = resort(list,move)
index = find_index(list,0,len(list)-1,target)

# project the index to initial index resorted before
if index==-1 :
	print -1
else :
	print (index+move-1)%len(list)+1