import random

N = 10
massiv = list()
for i in range(0,N):
	x = random.randint(-10,10)
	massiv.append(x)
print(massiv)
k = 0
for i in range(0,N):
	if (massiv[i] < 0):
		k = i
		break
#print(k)
summa = 0
for i in range(k+1,N):
	if (massiv[i] < 0):
		summa = summa - massiv[i]
	else:
		summa = summa + massiv[i]
print(summa)