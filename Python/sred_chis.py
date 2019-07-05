print ("Введите три числа ")
x = int(input("Первое число: "))
y = int(input("Второе число: "))
z = int(input("Третье число: "))

if ((x>y) and (x<z)) or ((x>z) and (x<y)):
	print("Cреднее число: " + str(x))
elif ((y>x) and (y<z)) or ((y>z) and (y<x)):
	print("Cреднее число: " + str(y))
elif ((z>y) and (z<x)) or ((z>x) and (z<y)):
	print("Cреднее число: " + str(z))
