import random

x = int(input("Введите количество строк матрицы: "))
y = int(input("Введите количество столбцов матрицы: "))

stroka = list()
stolbec = list()

for i in range(0,x):
	for j in range(0,y):
		chislo = random.randint(10,99)
		stroka.append(chislo)
	print(stroka)
	stolbec.append(stroka)
	stroka = list()

summa_list = list()
summa = 0
for j in range(0,y):
	for i in range(0,x):
		summa = summa + stolbec[i][j]
	summa_list.append(summa)
	summa = 0

index = 0
max = 0

for i in range(0,y):
	if summa_list[i] > max:
		max = summa_list[i]
		index = i
#print(summa_list)
print("Максимальная сумма в " + str(index + 1) + " столбце и равна: " + str(max))		


#print(stolbec[2])