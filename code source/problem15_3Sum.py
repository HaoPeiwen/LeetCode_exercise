def sum3(S):
	list = []
	for i in range(len(S)-2):
		#bruce forth
		for j in range(i+1,len(S)-1,1):
			for k in range(j+1,len(S),1):
				if S[i]+S[j]+S[k]==0 :
					x = sorted([S[i],S[j],S[k]])
					# get unique item
					if x not in list:
						list.append(x)
	return list
S = [-1, 0, 1, 2, -1, -4]
print sum3(S)