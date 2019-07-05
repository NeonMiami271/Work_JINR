#Решение квадратного уравнения
import math
print("Решим квадратное уравнение")
a = float(input("а = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - (4*a*c)

if D < 0:
	print("Корней нет")
elif D == 0:
	x = -b/(2*a)
	print("Корень равен:" + str(x))
elif D > 0:		
	x1 = (-b - math.sqrt(D))/(2*a)
	print("Первый корень равен: " + str(x1))
	x2 = (-b + math.sqrt(D))/(2*a)
	print("Второй корень равен: " + str(x2))