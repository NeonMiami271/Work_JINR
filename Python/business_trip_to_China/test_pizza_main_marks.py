import itertools
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random

#Пицца
pizza = ['Маргарита',
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
		[10,2,0,2,1,1,7,10,9,3], 
		[2,8,2,4,9,0,4,6,5,1],
		[7,7,10,9,1,2,1,6,5,10],
		[1,7,2,8,0,10,3,0,9,10],
		[3,6,2,9,2,3,5,8,1,9],
		[3,5,10,4,10,10,1,6,3,1], 
		[3,6,2,9,2,3,5,8,1,9], 
		[3,5,10,4,10,10,1,0,3,10],
		[1,1,9,8,4,9,5,9,2,4],
		[7,4,6,2,8,9,3,7,2,9],
		[10,1,2,7,6,5,2,9,3,1],
		[3,6,2,9,2,3,5,8,1,9], 
		[3,5,10,4,10,10,0,6,3,3], 
		[10,2,6,2,1,1,7,10,9,3], 
		[2,8,2,4,9,10,4,6,5,1],
		[3,5,10,4,0,10,1,6,3,5],
		[1,1,9,8,4,9,5,9,2,4],
		[7,4,6,0,8,9,3,7,2,9],
		[10,1,2,7,6,5,2,9,0,1]]

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

print("\n")
main_vector = list()
for i in range (0,len(pizza)):
	sum = 0
	for j in range (0, len(mark)):
		sum = sum + mark[j][i]
	sum = sum/100
	main_vector.append(sum)

print("Средние значения: " + str(main_vector))

sum = 0
for i in range (0,len(main_vector)):
	sum = sum + main_vector[i]

print("Сумма средних: " + str(sum))
print("Среднее средних: " + str(sum/len(pizza)))

main_vector_round = list()

max = 0
min = 10
min_index = 0
max_index = 0

for i in range(0,len(main_vector)):
	
	if main_vector[i]>max:
		max = main_vector[i]
		max_index = i

	if main_vector[i]<min:
		min = main_vector[i]
		min_index = i	

print("Максимальное значение: " + str(max) + ", индекс: " + str(max_index))
print("Минимальное значение: " + str(min) + ", индекс: " + str(min_index))

for i in range (0,len(main_vector)):
	main_vector_round.append(round(main_vector[i]))


print("Округленный ряд: " + str(main_vector_round))
print("******************************************************")
for i in range(0, len(pizza)):
	print(str(pizza[i]) + ": " + str(main_vector_round[i]))
print("******************************************************")

if (main_vector_round[min_index]>0):
	main_vector_round[min_index] = main_vector_round[min_index] - 1
	main_vector_round[max_index] = main_vector_round[max_index] + 1

print("******************************************************")
for i in range(0, len(pizza)):
	print(str(pizza[i]) + ": " + str(main_vector_round[i]))
print("******************************************************")



