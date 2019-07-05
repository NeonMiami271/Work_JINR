import math
def perevod(number):
	a = str(number)
	length = len(a)
	#print(length)
	sum = 0
	i=0
	while i<length:
		
		#print(a[i])
		sum = sum + int(a[i]) * int(2**(length-1-i))
		i=i+1

	return print("Ответ: " + str(sum))

k = int (input("ВВедите двоичное число: "))
perevod(k)