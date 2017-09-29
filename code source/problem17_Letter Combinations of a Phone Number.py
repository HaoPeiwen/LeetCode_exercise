import itertools

# alphabet
def numbers_to_strings(argument):
    switcher = {
        '2' : ['a','b','c'],
        '3' : ['d','e','f'],
        '4' : ['g','h','i'],
        '5' : ['j','k','l'],
        '6' : ['m','n','o'],
        '7' : ['p','q','r','s'],
        '8' : ['t','u','v'],
        '9' : ['w','x','y','z']
    }
    return switcher.get(argument,'Nothing')

# Cartesian product
def combination(string):
	list = ['']
	for i in range(len(string)):
		temp = []
		for x in itertools.product(list,numbers_to_strings(string[i])):
			temp.append(x[0]+x[1])
		list = temp
	return list

string = '234'
print combination(string)