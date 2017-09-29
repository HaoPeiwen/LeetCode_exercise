def show(integer,length):
		for i in range(length-1,-1,-1):
			if i == 0 :
				print integer[0]
			else:
				print integer[i],'->',
class add_integers:
	def __init__(self,int1,int2):
		self.int1 = int1
		self.len1 = len(int1)
		self.int2 = int2
		self.len2 = len(int2)
	def add(self):
		show(self.int1,self.len1)
		show(self.int2,self.len2)
		t = 0
		if self.len1>self.len2:
			self.int2 = '0'*(self.len1-self.len2)+self.int2
		else:
			self.int1 = '0'*(self.len2-self.len1)+self.int1

		for i in range(self.len1-1,-1,-1):
			temp = ord(self.int1[i])-ord('0')+ord(self.int2[i])-ord('0')+t
			print temp%10,
			t = temp/10
			if i>0:
				print '->',
		if t>0:
			print '->',t

example = add_integers("342","465")
example.add()

