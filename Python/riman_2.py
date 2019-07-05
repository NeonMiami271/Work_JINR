#import numpy
import random


x2 = 0
x1 = 0
n = 0
sum = 0
i = 0

a = 0
b = 5
step = 0.5

while x2 < b:
	n = n + 1
	x2 = x2 + step
	
	if n == 1: x1 = 0
	else: x1 = a + x2 - step
	
	k = random.uniform(x1,x2)
	sum = sum + k * (x2 - x1)
	#print(str(n) + ". " + str (k * (x2 - x1)))

print("-----------------------------------------------------------")
print("Интеграл в диапозоне от " + str(a) + " до " + str(b) + " с шагом " + str(step) + " по Римману равен: " + str(sum))
print("Количество шагов: " + str(n))