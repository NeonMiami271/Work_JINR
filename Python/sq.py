import math
print("ВВедите стороны треугольника:")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

if ((a+b)<=c) or ((a+c)<=b) or ((b+c)<=a):
	print("Треугольника с такими сторонами не существует")
else:
	p=float((a+b+c)/2)
	s=math.sqrt(p*(p-a)*(p-b)*(p-c))

	print("Площадь равна: "+ str("%.2f" % s))