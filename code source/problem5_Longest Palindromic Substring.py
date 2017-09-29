def LPS(initial_string):
	all_list=[]
	#odd detection
	for i in range(len(initial_string)):
		#print i,'i---'
		flag = 1
		for j in range(min(len(initial_string)-i,i+1)):
			temp = j
			if initial_string[i-temp]!=initial_string[i+temp]:
				flag = 0
				break
		if flag == 0 :
			temp -= 1
		#print temp,'temp----'
		all_list.append(initial_string[i-temp:i+temp+1])

	#even detection
	for i in range(len(initial_string)-1):
		#print i,'i---'
		if initial_string[i] == initial_string[i+1]:
			flag = 1
			for j in range(min(len(initial_string)-1-i,i+1)):
				temp = j
				if initial_string[i-temp]!=initial_string[i+1+temp]:
					flag = 0
					break
			if flag == 0 :
				temp -= 1
			#print temp,'temp----'
			all_list.append(initial_string[i-temp:i+temp+2])

	#find_max
	max_length = 0
	max_string = ''
	for i in range(len(all_list)):
		if len(all_list[i])>max_length:
			max_length = len(all_list[i])
			max_string = all_list[i]

	print 'all_substring:',
	#get_all
	for i in range(len(all_list)):
		if len(all_list[i]) == max_length:
			print all_list[i],


#full_string = 'abcbattaba'
#full_string = 'babad'
full_string = 'cbbd'
LPS(full_string)

