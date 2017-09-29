def zigzag_adjust(full_string):
	for i in range(0,len(full_string),4):
		print full_string[i],
	for i in range(1,len(full_string),2):
		print full_string[i],
	for i in range(2,len(full_string),4):
		print full_string[i],

full_string = "PAYPALISHIRING"
zigzag_adjust(full_string)
