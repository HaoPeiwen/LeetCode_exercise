def generate(string,need):
	# string: prefix
	# left: number of "("
	# right: number of ")"
	# need: still need |need| "("s or ")"s to fill the string

	# analyze the string
	left = 0
	right = 0
	for i in string:
		if i ==")":
			right += 1
		else:
			left += 1

	# classify and implement every classification
	list=[]
	if left==right:
		list.append(string+"(")
	elif left==right+need :
		list.append(string+")")
	elif left>right and left<right+need:
		list.append(string+")")
		list.append(string+"(")
	return list


def main(n):
	#initial
	list = [""]
	for i in range(2*n):
		temp = []
		for j in list:
			t = generate(j,2*n-i)
			if len(t)!=0 :
				# get all the possible return in round i
				temp += t
		list = temp

	print list

main(5)



