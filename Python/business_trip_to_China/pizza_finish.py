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
		[10,2,1,2,1,1,7,10,9,3], 
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

L_max = -1.0
L_iterac = -1.0
result_applicant = ""
x = list()
store = list()
store_L = list()

middle_value = []

for i in range(0,len(pizza)):
	sum = 0
	for j in range(0,len(mark)):
		sum = sum + mark[j][i]
	#print(sum)
	middle_value.append(sum)

with open('combinations.txt') as my_file:
	data = []
	for line in my_file:
		line = line.split() # to deal with blank 
		if line:            # lines (ie skip them)
			line = [int(i) for i in line]
			data.append(line)
		#print(str(line))

#print(data)

now = 0


for i in range(0,len(data)):

	L_iterac = 1
	for j in range(0, len(data[i])):	

		#print(sum)
		L_iterac = L_iterac * data[i][j] / middle_value[j]


	#x.append(L_iterac)
	if L_iterac > L_max: 
		L_max = L_iterac
		result_applicant = data[i]
	#	store.append(data)
	#	store_L.append(L_max)

	print(str(data[i]) + "   " + "      " + str(L_iterac) + "     " + str(L_max) + "\n")

print(str(result_applicant))