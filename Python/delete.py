import random
z = int(input("ВВедите количество элементов массива: "))
x = int(input("ВВедите начало интервала удаления: "))
y = int(input("ВВедите конец интервала удаления: "))
N = z
massiv = list()
for i in range(0,z):
	chislo = random.randint(0,100)
	massiv.append(chislo)
print(massiv)
i = 0
k = 0
while i<z:
	if (massiv[i] > x) and (massiv[i] < y):
		del(massiv[i])
		z = z - 1
		k = k + 1
	else:
		i = i + 1

for i in range(z,N):
	massiv.append(0)
print(massiv)

