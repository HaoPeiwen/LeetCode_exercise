def divide(divided,divider):
	length = len(divided)
	len1 = len(divided)
	len2 = len(divider)
	index1 = 0
	index2 = 1
	i = 0
	# save the result
	shang = []

	# move foreward
	while index2<length :
		while not judge(divided[index1:index2],divider) and index2<length :
			index2 += 1
			# when it comes to that 12345600000000001/123456 so that there
			# will have a lot of zeros in the result, so we push the index1
			if index1<length-1 and divided[index1]=='0' :
				index1 += 1
				shang.append('0')

		# one small piece divide
		sub,move,result = minus(divided[index1:index2],divider)
		#print sub,move,result,index1,index2,

		#change the divided
		if index1<1 :
			divided = sub+divided[index2:]
		else :
			divided = divided[:index1]+sub+divided[index2:]
		#print divided
		index1 += move
		shang.append(str(result))

	# move the prefix zeros in result
	while len(divided)>0 and divided[0]=='0' :
		divided = divided[1:]
	return 'result:'+''.join(shang),'rest:'+divided

# judge the weigh of subinteger
def judge(sub1,sub2):
	if len(sub1)<len(sub2) :
		return 0
	elif len(sub1)==len(sub2) :
		flag = 1
		for i in range(len(sub1)) :
			if sub1[i]<sub2[i] :
				flag = 0
				break
			elif sub1[i]>sub2[i] :
				flag = 1
				break
		return flag
	else :
		return 1

# piece - divider
# return iters and sub2
def minus(sub1,sub2):
	temp = sub1
	sub1 = []
	for i in temp :
		sub1.append(i)
	temp = sub2
	sub2 = []
	for i in temp :
		sub2.append(i)

	result = 0 
	move = 0
	while judge(sub1,sub2) : 
		for i in range(1,len(sub2)+1,1):
			if ord(sub1[-i])<ord(sub2[-i]) :
				sub1[-i] = chr(10+ord(sub1[-i])-ord(sub2[-i])+ord('0'))
				sub1[-i-1] = chr(ord(sub1[-i-1])-1)
			else :
				sub1[-i] = chr(ord(sub1[-i])-ord(sub2[-i])+ord('0'))
		result += 1
		while len(sub1)>0 and sub1[0]=='0' :
			move += 1
			sub1 = sub1[1:]
	temp ='0'*move+''.join(sub1)
		#print temp,sub1
	#print temp,move,result
	return temp,move,result


integer1 = '12345678987654321'
integer2 = '111111111'
#print judge(integer1,integer2)
print divide(integer1,integer2)
#print divide('1000','33')