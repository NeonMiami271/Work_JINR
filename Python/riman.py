#import numpy
import random

n = 0
sum = 0
i = 0
arg = 0

a = -5
b = 5
step = 0.0001

N = (b - a)//step
x1 = a
x2 = 0

while i < N:
	i = i + 1
	x1 = x1 + step
	
	if i == 1: x2 = a
	else: x2 = x1 - step
	
	k = random.uniform(x1,x2)

	arg = k * (x2 - x1)
	if arg < 0: arg = arg * (-1)
	sum = sum + arg

	print(str(i) + ". " + str (arg))

print("-----------------------------------------------------------")
print("Интеграл в диапозоне от " + str(a) + " до " + str(b) + " с шагом " + str(step) + " по Римману равен: " + str(sum))
print("Количество шагов: " + str(i))


#print("blablabla {0:.2f}".format(sum))