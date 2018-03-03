# if target in list
def Found(list,target,start_index,end_index):
	if start_index>end_index :
		return -1
	elif start_index==end_index and target==list[start_index] :
		return start_index
	elif start_index==end_index and target!=list[start_index] :
		return -1
	else :
		mid = (start_index+end_index)/2
		if list[mid]==target :
			return mid
		elif list[mid]<target :
			return Found(list,target,mid+1,end_index)
		else :
			return Found(list,target,start_index,mid-1)

# if target not in list
def Insert(list,target,start_index,end_index):
	if start_index+1==end_index :
		return start_index
	else :
		mid = (start_index+end_index)/2
		if list[mid]==target :
			return mid
		elif list[mid]<target :
			return Insert(list,target,mid+1,end_index)
		else :
			return Insert(list,target,start_index,mid-1)

def Sythesis(list,target,start_index,end_index):
	if list[0]>target :
		return 0
	elif list[-1]<target :
		return len(list)
	else :
		back = Found(list,target,start_index,end_index)

	# if target not in list
	if back!=-1 :
		return back
	else :
		return Insert(list,target,start_index,end_index)
list = [1,2,6,7]
for i in range(10):
	print i,'->',Sythesis(list,i,0,len(list)-1)