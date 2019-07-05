import itertools

#Месяцы
month = ['Февраль',
		 'Март',
		 'Апрель',
		 'Май',
		 'Июнь',
		 'Июль']


#Прентенденты
applicant = ['Sharov',
			 'Rubnikov',
			 'Selynin',
			 'Butorov',
			 'Chetverikov',
			 'Korablev']

#Оценки
mark = [[1,10,5,8,7,4], 
		[1,3,2,8,9,4], 
		[10,1,1,9,10,1],
		[5,7,9,1,2,6],
		[6,2,8,9,9,8],
		[8,7,1,2,7,10]]

#Коэффициенты
koef = [0.5, 
		1.0, 
		1.0, 
		0.7, 
		0.5, 
		1.0]



combinations = list(itertools.permutations(applicant, len(applicant)))
#print (str(combinations))

#Вывод всех возможных комбинаций
#for i in range(0, len(combinations)):       
#	print(str(combinations[i]) + "\n")

L_max = -1.0
L_iterac = -1.0
result_applicant = ""

for i in range(0, len(combinations)):
	#print(str(L_iterac) + " " + str(L_max) + "\n")
	if L_iterac > L_max: 
		L_max = L_iterac
		result_applicant = combinations[i]

	L_iterac = 1
	for j in range(0, len((combinations[i]))):	
		if combinations[i][j] == 'Sharov': index = 0
		if combinations[i][j] == 'Rubnikov': index = 1
		if combinations[i][j] == 'Selynin': index = 2
		if combinations[i][j] == 'Butorov': index = 3
		if combinations[i][j] =='Chetverikov': index = 4
		if combinations[i][j] == 'Korablev': index = 5
		
		#print(str(sum) + "\n")
		sum = 0
		for k in range(0,len(mark[index])):
			sum = sum + mark[index][k]
		
		L_iterac = L_iterac * (koef[index]*mark[index][j]/sum)

#print(str(result_applicant))
print("\n**************************************************************")
for number in range(0,len(result_applicant)):
	print(str(month[number]) + " - " + str(result_applicant[number]))
print("\n**************************************************************")

#print()
#print("Всего возможных комбинаций: " + str(len(combinations)))
#print()