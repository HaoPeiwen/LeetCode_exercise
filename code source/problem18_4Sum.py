def sum4(S,target):
	list = []
	for i in range(len(S)-3):
		#bruce forth
		for j in range(i+1,len(S)-2,1):
			for k in range(j+1,len(S)-1,1):
				for l in range(k+1,len(S),1):
					if S[i]+S[j]+S[k]+S[l]==target :
						x = sorted([S[i],S[j],S[k],S[l]])
						# get unique item
						if x not in list:
							list.append(x)
	return list
S = [1, 0, -1, 0, -2, 2]
target = 0
print sum4(S,target)