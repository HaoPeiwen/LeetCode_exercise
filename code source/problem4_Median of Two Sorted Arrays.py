# -*- coding: cp936 -*-
def median(nums1,nums2):
	m = len(nums1)
	n = len(nums2)
	if m<n: #确保nums1比较长
		m,n = n,m
		nums1,nums2 = nums2,nums1
	if nums1[-1]<nums2[0] : #如果nums1中最大小于nums2中最小
		new = nums1+nums2
		new1 = new[:(m+n+1)/2]
		new2 = new[(m+n+1)/2:]
	elif nums2[-1]<nums1[0] : #如果nums2中最大小于nums1中最小
		new = nums1+nums2
		new1 = new[:(m+n+1)/2]
		new2 = new[(m+n+1)/2:]
	#如果nums2不可分割（左）
	elif (m/2-len(nums2)-1>=0) & (nums2[-1]<nums1[m/2-len(nums2)]):
		new1 = sorted(nums1[:(m+1)/2-len(nums2)+1]+nums2)
		new2 = nums1[(m+1)/2-len(nums2)+1:]
	#如果nums2不可分割（右）
	elif (m/2+len(nums2)-1<m) & (nums2[0]>nums1[m/2+len(nums2)]):
		new1 = nums1[:(m+1)/2+len(nums2)-1]
		new2 = sorted(nums1[(m+1)/2+len(nums2)-1:]+nums2)
	else:#nums2可分割
		imin = 0 
		imax = m
		i = (imin+imax+1)/2
		j = (m+n+1)/2-i
		while nums1[i-1]>nums2[j] or nums2[j-1]>nums1[i] :
			if nums1[i-1]>nums2[j]:
				print 1
				imax = i
				i = (imin+imax+1)/2
				j = (m+n+1)/2-i
			else:
				print 2
				imin = i
				i = (imin+imax+1)/2
				j = (m+n+1)/2-i
		new1 = sorted(nums1[:i]+nums2[:j])
		new2 = sorted(nums1[i:]+nums2[j:])
	print new1
	print new2
	print 'median',
	if len(new1)%2==0 :
		return float(new1[-1]+new2[0])/2
	else:
		return new1[-1]
nums1=[1,2,3,6,9,11,12,14,15,17,18,19,20,21,22]
nums2=[100,101]
print median(nums1,nums2)

