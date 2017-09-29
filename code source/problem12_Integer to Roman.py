def RomRank(integer):
	Roman=''
	if integer==0 :
		Roman = ''
	elif 1<=integer and integer<=3 :
		Roman = 'I'*integer
	elif integer==4 :
		Roman = 'IV'
	elif 5<= integer and integer<=8 :
		Roman = 'V'+'I'*(integer-5)
	elif integer==9 :
		Roman = 'IX'
	elif 10<= integer and integer <=30 and integer%10==0:
		Roman = 'X'*(integer/10)
	elif integer==40:
		Roman = 'XL'
	elif 50<= integer and integer <=80 and integer%10==0:
		Roman = 'L' + 'X'*(integer/10-5)
	elif integer==90:
		Roman = 'XC'
	elif 100<= integer and integer <=300 and integer%100==0:
		Roman = 'C'*(integer/100)
	elif integer==400:
		Roman = 'CD'
	elif 500<= integer and integer <=800 and integer%100==0:
		Roman = 'D' + 'C'*(integer/100-5)
	elif integer==900:
		Roman = 'CM'	
	elif 1000<= integer and integer <=3000 and integer%100==0:
		Roman = 'M'*(integer/1000)
	return Roman

def int2Rom(integer):
	string=[]
	length = len(str(integer))-1
	while length>=0 :
		string.append(integer/(10**length)*(10**length))
		integer = integer%(10**length)
		length -= 1
		
	Roman=''
	for i in range(len(string)):
		Roman = Roman+RomRank(string[i])
	return Roman

integer1=520
integer2=1314
print int2Rom(integer1)+'_'+int2Rom(integer2)