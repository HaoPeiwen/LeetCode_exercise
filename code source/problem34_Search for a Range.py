# find one point that are equal to target
def Search(list,target,start_index,end_index):
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
			return Search(list,target,mid+1,end_index)
		else :
			return Search(list,target,start_index,mid-1)

# find the left_index
def Search_left(list,target,start_index,end_index):
	if start_index>end_index :
		return -1
	elif start_index==end_index and target==list[start_index] :
		return start_index
	elif start_index==end_index and target!=list[start_index] :
		return -1
	else :
		mid = (start_index+end_index)/2
		if list[mid]<target :
			return Search(list,target,mid,end_index)
		else :
			return Search(list,target,start_index,mid)

# find the right_index
def Search_right(list,target,start_index,end_index):
	if start_index>end_index :
		return -1
	elif start_index==end_index and target==list[start_index] :
		return start_index
	elif start_index==end_index and target!=list[start_index] :
		return -1
	else :
		mid = (start_index+end_index)/2
		if list[mid]>target :
			return Search(list,target,start_index,mid)
		else :
			return Search(list,target,mid,end_index)



list = [5,7,7,8,8,8,8,8,10]
target = 8
# get mid_index
mid_index = Search(list,target,0,len(list)-1)
left_index = Search_left(list,target,0,mid_index)
right_index = Search_right(list,target,mid_index,len(list)-1)
print [left_index,right_index]