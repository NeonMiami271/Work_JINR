import random

n1 = int(input('ВВедите первую границу массива: '))
n2 = int(input('ВВедите вторую границу массива: '))
numb = int(input('ВВедите количество элемнтов массива: '))
n=0
if (numb<=2):
		print('Для сортировки не хватает элементов')
		
		
else:
	a=list()
	while n<numb:
		x=random.randrange(n1,n2)
		a.append(x)
		n = n + 1
	print('Исходный массив: ')	
	print(a)
	print('Элементы отсортированны по возрастанию: ')
	a.sort()
	print(a)
	print('Элементы отсортированны по убыванию: ')
	a.reverse()
	print(a)

	
