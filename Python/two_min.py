import random

massiv = list()
min_1 = 101
min_2 = 101
N = 10
k = 0
for i in range(0,N):
	x = random.randint(0,100)
	massiv.append(x)

print(massiv)

for i in range(0,N):
	if (massiv[i] < min_1):
		min_1 = massiv[i]
		k = i
massiv[k] = 101

for i in range(0,N):
	if (massiv[i] < min_2):
		min_2 = massiv[i]

print("Минимальные элементы массива: " + str(min_1) + " и " + str(min_2))			