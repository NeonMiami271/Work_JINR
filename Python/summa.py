n=int(input("До какого числа ищем сумму? "))
k = 0
sum = 0
while k<=n:
	sum = sum + k
	k = k + 1
print('Сумма от 1 до '+str(n)+" равна "+str(sum))
