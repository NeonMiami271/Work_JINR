import random
N = 100
x = list()
y = list()
sum = 0
for i in range(0,N):
	a = random.randint(0,100)
	x.append(a)
	sum = sum + x[i]
sred = sum / N
print(x)
print("Среднее значение равно: " + str("%.2f" % sred))	

for i in range(0,N):
	if (x[i] < sred):
		y.append(x[i])
print(y)		
