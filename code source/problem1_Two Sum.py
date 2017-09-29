def p1(nums,target):
	for i in range(len(nums)):
		for j in range(i):
			if(nums[i]+nums[j] == target):
				return [j,i]

nums = [2,7,11,15]
target = 9 
print p1(nums,target)