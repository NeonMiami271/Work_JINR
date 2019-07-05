x = str(input("ВВедите число: "))
k = 0
sum = 0
while k<len(x):
	sum = sum + int(x[k])
	k = k + 1
print("Сумма цифр в числе "+ str(x) + " равна " + str(sum))