def isPalNum(integer):
	# judge is negative
	if integer<0:
		return 'negative'
	while len(str(integer))>1:
		# if head and tail is equal, then delete both
		if integer/(10**(len(str(integer))-1)) == integer%10:
			integer = integer%(10**(len(str(integer))-1))/10
	    # else is not palindrome
		else:
			break
	if len(str(integer))<=1 :
		return 'yes'
	else:
		return 'no'


#integer = 12344321
integer = -12354321
print isPalNum(integer)

