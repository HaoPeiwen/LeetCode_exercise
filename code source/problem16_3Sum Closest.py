def sum3_closest(S,target):
	list = []
	epsilon = 1000
	for i in range(len(S)-2):
		#bruce forth to get decrease list
		for j in range(i+1,len(S)-1,1):
			for k in range(j+1,len(S),1):
				if S[i]+S[j]+S[k]-target>=0 and S[i]+S[j]+S[k]-target<=epsilon :
					epsilon = S[i]+S[j]+S[k]-target
					x = sorted([S[i],S[j],S[k]])
					# get unique item
					if x not in list:
						list.append(x)
				elif S[i]+S[j]+S[k]-target<0 and S[i]+S[j]+S[k]-target>=(-1)*epsilon :
					epsilon = -S[i]-S[j]-S[k]+target
					x = sorted([S[i],S[j],S[k]])
					# get unique item
					if x not in list:
						list.append(x)
	# get a new list int which items have the difference "epsilon"
	list_new = []
	for i in range(len(list)-1,-1,-1):
		if abs(sum(list[i])-target)<target+	0.1 :
			list_new.append(list[i])
		else :
			break
	return list_new
S = [-1,-4,1,2]
target = 1
print sum3_closest(S,target)