class oper:

	def case(self, x, y, z):

		self.x = float(x)
		self.y = str(y)
		self.z = float(z)

		if self.y == '+':
			print(float(self.x)+float(self.z))
		elif self.y=='-':
			print(float(self.x)-float(self.z))
		elif self.y=='*':
			print(float(self.x)*float(self.z))
		elif self.y=='/':
			print(float(self.x)/float(self.z))
		else: 
			print ("Неизвестная операция")