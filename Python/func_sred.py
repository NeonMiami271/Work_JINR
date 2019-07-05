import random


def sred(massiv):
	N = 10
	sum = 0
	for i in range(0,N):
		x = random.randint(-100,100)
		massiv.append(x)
	print(massiv)	
	for i in range (0,N):
		sum = sum + massiv[i]
	d = sum / N
	return print("Среднее знвчение массива равно: " + str("%.2f" % d))		


k = list()
sred(k)
