n = int(input("Введите количеств позиций из которых будет состоять выбор "))
position = list()
for i in range(0,n):
	x = str (input(str(i+1) + ". "))
	position.append(x)
print(str(position))


n = int(input("Введите количество участников опроса "))
marks = list()
for i in range(0,n):
	print(str(i+1) + ". ")
	for j in range(0,len(position)):
		x = int (input())
		marks[i].append(x)
print(str(marks))

