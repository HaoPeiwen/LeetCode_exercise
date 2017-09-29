def Rank2num(rank):
	if rank=='I':
		return 1
	elif rank=='V':
		return 5
	elif rank=='X':
		return 10
	elif rank=='L':
		return 50
	elif rank=='C':
		return 100
	elif rank=='D':
		return 500
	elif rank=='M':
		return 1000

def Rom2Int(Roman):
	sum = 0
	# judge whether the character is smaller than the former
	for i in range(len(Roman)-1):
		if Rank2num(Roman[i])<Rank2num(Roman[i+1]) :
			sum = sum - Rank2num(Roman[i])
		else :
			sum = sum + Rank2num(Roman[i])
	sum = sum + Rank2num(Roman[-1])
	return sum

#Roman='MCCCXIV'
Roman='DXX'
print Rom2Int(Roman)