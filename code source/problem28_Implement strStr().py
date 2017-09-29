def find_needle(haystack,needle):
	if len(needle)==0 :
		return 0
	elif len(needle)>len(haystack) :
		return -1
	else :
		for i in range(len(haystack)-len(needle)) :
			flag = 0
			for j in range(len(needle)) :
				if haystack[i+j]!=needle[j] :
					flag = 1
					break
			if flag == 0 :
				return i

haystack = 'zhouyiran_I_love_you_by_yangchaoqi'
needle = 'love'
print find_needle(haystack,needle)