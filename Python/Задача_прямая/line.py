
class linee:

	def __init__(self, x1, y1, x2, y2):
		
		self.x1 = float (x1)
		self.y1 = float (y1)
		self.x2 = float (x2)
		self.y2 = float (y2)

		k = (self.y1 - self.y2)/(self.x1 - self.x2)
		b = self.y2 - k*self.x2

		print("----------------------------------------------------")
		print("Уравнение прямой: " + str(k) + "*X" + " + " + str(b) )
		print("----------------------------------------------------")



