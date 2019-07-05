import random
N = 5
max = 0
x = list()

for i in range (0,N):
	a = random.randint(-100,100)
	x.append(a)
print(str(x))

for i in range (0,N):
	if ((i+1) % 2 == 0) and (x[i] > max):
		max = x[i]
print("Ответ: " + str(max))
