import numpy as np
def get_height(n):
	return np.random.rand(n,1)*10

def get_container(n):
	height = get_height(n)
	index = [i for i in range(n)]
	max_container = 0
	max_left = 0
	max_right = 0 
	for i in range(n):
		for j in range(i):
			temp = (i-j)*min(height[i],height[j])
			if temp>max_container :
				max_container = temp
				max_left = j
				max_right = i

	print 'index',index
	print 'height',height
	print 'index=','[',max_left+1,',',max_right+1,']','container=',max_container

get_container(10)
