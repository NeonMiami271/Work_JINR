import itertools

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
mark = [[2,1,7,10,10], 
		[1,9,9,5,1], 
		[4,10,4,2,1],
		[3,10,2,9,8],
		[1,4,7,9,10],
		[1,10,5,1,10]]

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

	if L_iterac > L_max: 
		L_max = L_iterac
		result_applicant = combinations[i]
		
	print(str(combinations[i]) + "   " + "      " + str(L_iterac) + "     " + str(L_max) + "\n")

#print(str(result_applicant))
print("\n**************************************************************")
for number in range(0,len(result_applicant)):
	print(str(month[number]) + " - " + str(result_applicant[number]))
print("\n**************************************************************")