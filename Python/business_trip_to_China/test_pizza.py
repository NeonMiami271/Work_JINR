import itertools
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#Пицца
month = ['Маргарита',
		 'Маринара',
		 'Наполетана',
		 'Каприциоза',
		 'Сицилия',
		 '4 Сыра',
		 'Классическая',
		 'Охотничья',
		 'Пепперони',
		 'Филадельфия']


#Прентенденты
applicant = ['Шаров',
			 'Рыбников',
			 'Селюнин',
			 'Буторов',
			 'Соколов',
			 'Кораблев',
			 'Четвериков',
			 'Анфимов',
			 'Кузнецова',
			 'Лавров',
			 'Леденев',
			 'Чашечкин',
			 'Сайфулин',
			 'Попов',
			 'Иванова',
			 'Самойлов',
			 'Морозова',
			 'Соколов',
			 'Чудакова',
			 'Рыбовалова']

#Оценки
mark = [[3,5,10,4,10,10,1,6,3,8], 
		[10,2,6,2,1,1,7,10,9,3], 
		[2,8,2,4,9,10,4,6,5,1],
		[7,7,10,9,1,2,1,6,5,10],
		[1,7,2,8,4,10,3,3,9,10],
		[3,6,2,9,2,3,5,8,1,9],
		[3,5,10,4,10,10,1,6,3,1], 
		[3,6,2,9,2,3,5,8,1,9], 
		[3,5,10,4,10,10,1,6,3,10],
		[1,1,9,8,4,9,5,9,2,4],
		[7,4,6,2,8,9,3,7,2,9],
		[10,1,2,7,6,5,2,9,3,1],
		[3,6,2,9,2,3,5,8,1,9], 
		[3,5,10,4,10,10,1,6,3,3], 
		[10,2,6,2,1,1,7,10,9,3], 
		[2,8,2,4,9,10,4,6,5,1],
		[3,5,10,4,10,10,1,6,3,5],
		[1,1,9,8,4,9,5,9,2,4],
		[7,4,6,2,8,9,3,7,2,9],
		[10,1,2,7,6,5,2,9,3,1]]

#Коэффициенты
koef = [1.0, 
		1.0, 
		1.0, 
		1.0, 
		1.0, 
		1.0,
		1.0, 
		1.0, 
		1.0, 
		1.0, 
		1.0,
		1.0, 
		1.0, 
		1.0, 
		1.0, 
		1.0,
		1.0, 
		1.0, 
		1.0, 
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
	
	now = 0
	L_iterac = 1
	for j in range(0, len((combinations[i]))):	
		index = applicant.index(combinations[i][j])
		

		
		sum = 0
		for k in range(0,len(mark[index])):
			sum = sum + mark[index][k]
		
		now = now + mark[index][j]/sum


	for j in range(0, len((combinations[i]))):	
		index = applicant.index(combinations[i][j])
		
		sum = 0
		for k in range(0,len(mark[index])):
			sum = sum + mark[index][k]

		L_iterac = L_iterac * (koef[index]*mark[index][j]/sum*(1/now))



	x.append(L_iterac)
	if L_iterac > L_max: 
		L_max = L_iterac
		result_applicant = combinations[i]
		store.append(combinations[i])
		store_L.append(L_max)
		
	#print(str(combinations[i]) + "   " + "      " + str(L_iterac) + "     " + str(L_max) + "\n")

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

