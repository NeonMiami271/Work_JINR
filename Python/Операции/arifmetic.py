def arithmetic(x,y,z):
	if y == '+':
		return float(x)+float(z)
	elif y=='-':
		return float(x)-float(z)
	elif y=='*':
		return float(x)*float(z)
	elif y=='/':
		return float(x)/float(z)
	else: 
		return ("Неизвестная операция")


