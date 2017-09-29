def reverse_int(integer):
	string = str(integer)
	recon = ''
	for i in range(len(string)-1,-1,-1):
		if i==0 and string[i]=='-':
			recon = '-'+recon
		else:
			recon = recon+string[i]
	print recon

integer = -123
reverse_int(integer)
