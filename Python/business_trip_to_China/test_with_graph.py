import itertools
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#Месяцы
month = ['Февраль',
		 'Март',
		 'Апрель',
		 'Май',
		 'Июнь']


#Прентенденты
applicant = ['Sharov',
			 'Rubnikov',
			 'Selynin',
			 'Butorov',
			 'Chetverikov',
			 'Korablev']

#Оценки
mark = [[3,5,10,4,10], 
		[1,10,10,4,3], 
		[7,10,4,1,3],
		[4,10,4,7,7],
		[0,4,9,10,10],
		[0,10,4,1,9]]

#Коэффициенты
koef = [0.25, 
		1.0, 
		1.0, 
		0.5, 
		0.25, 
		1.0]



combinations = list(itertools.permutations(applicant, 5))

#print (str(combinations))

#Вывод всех возможных комбинаций
#for i in range(0, len(combinations)):       
#	print(str(combinations[i]) + "\n")

L_max = -1.0
L_iterac = -1.0
result_applicant = ""
x = list()
store = list()
store_L = list()

for i in range(0, len(combinations)):
	
	L_iterac = 1
	for j in range(0, len((combinations[i]))):	
		if combinations[i][j] == 'Sharov':      index = 0
		if combinations[i][j] == 'Rubnikov':    index = 1
		if combinations[i][j] == 'Selynin':     index = 2
		if combinations[i][j] == 'Butorov':     index = 3
		if combinations[i][j] == 'Chetverikov': index = 4
		if combinations[i][j] == 'Korablev':    index = 5
		
		sum = 0
		for k in range(0,len(mark[index])):
			sum = sum + mark[index][k]
		
		L_iterac = L_iterac * (koef[index]*mark[index][j]/sum)

	x.append(L_iterac)
	if L_iterac > L_max: 
		L_max = L_iterac
		result_applicant = combinations[i]
		store.append(combinations[i])
		store_L.append(L_max)
		
	print(str(combinations[i]) + "   " + "      " + str(L_iterac) + "     " + str(L_max) + "\n")

#print(str(result_applicant))
#print("\n**************************************************************")
#for number in range(0,len(result_applicant)):
#	print(str(month[number]) + " - " + str(result_applicant[number]))
#print("\n**************************************************************")
#print(str(x))

print("\n**************************************************************")
for number_1 in range(2,len(store)):
	print("\n")
	for number_2 in range(0,len(store[number_1])):
		print(str(month[number_2]) + " - " + str(store[number_1][number_2]))
print("\n**************************************************************")

num_bins = 500
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.7)
plt.show()



