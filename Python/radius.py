#Принадлежность точки окружности

import math
r = int(input("ВВедите радиус окружности: "))
x = int(input("x= "))
y = int(input("y= "))

D = math.sqrt(x**2 + y**2)

if D < r:
	print("Точка лежит внутри окружности")
elif D == r:
	print("Точка лежит на окружности")
elif D > r:
	print("Точка лежит за пределами окружности")


			