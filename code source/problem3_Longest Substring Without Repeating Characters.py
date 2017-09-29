def find_sub(full_string,length):
	if length == 1:
		return full_string,length
	else:
		temp1_str,temp1_len = find_sub(full_string[:-1],length-1)
		temp2_str = full_string[-1]
		temp2_len = 1
		for i in range(length):
			list_count = [0]*26
			extract_len = length-i
			extract_str = full_string[i:]
			for i in range(len(extract_str)):
				list_count[ord(extract_str[i])-ord('a')] += 1
			list_count = sorted(list_count)
			if list_count[-1] ==1:
				temp2_str = extract_str
				temp2_len = extract_len
				break
		if temp1_len > temp2_len:
			return temp1_str, temp1_len
		else:
			return temp2_str, temp2_len

#full_string = 'abcabcbb'
#full_string = 'bbbbbbbbb'
full_string = 'pwwkew'
print find_sub(full_string, len(full_string))

