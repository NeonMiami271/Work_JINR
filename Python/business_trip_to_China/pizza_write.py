import itertools
from itertools import cycle
import random


my_file = open("comb_test.txt", "w+")

N = 100000000
sum_2 = 0
results = list()
for i in range (0,N):
	print(str(N-i))
	sum = 0
	pizza = list()
	#print(str(i))
	
	for j in range(0, 10):
		pizza.append(random.randint(0,10))
		sum = sum + pizza[j]

	#print(pizza)
	if sum == 10: 
		sum_2 = sum_2 + 1
		results.append(pizza)
		for k in range(len(pizza)):
			my_file.write(str(pizza[k]) + " ")
		my_file.write("\n")

print("Всего таких рядов: " + str(sum_2))
my_file.close()