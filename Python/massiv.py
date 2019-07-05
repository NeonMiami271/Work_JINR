import random
mas = list()
N = 3

for i in range (0,N):
	x = random.randint(-100,100)
	mas.append(x)
sum = 0
for i in range (0,N):
	if (mas[i] > 0) and (mas[i] % 2 == 0):
		sum = sum + mas[i]

print(str(mas))
print("Ответ: " + str(sum))