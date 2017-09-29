def valid(string):
	# use a stack
	stack = ''
	for i in string:
		if len(stack)==0 and (i==')' or i==']' or i=='}'):
			return 'not pass'
			break
		#pop
		if i==')' and stack[-1]=='(':
			stack = stack[:-1]
		elif i==']' and stack[-1]=='[':
			stack = stack[:-1]
		elif i=='}' and stack[-1]=='{':
			stack = stack[:-1]
		else:
		#push
			stack = stack+i
		print stack
	if len(stack)==0:
		return 'pass'

string = "({(((({})[])))}[])"
print valid(string)