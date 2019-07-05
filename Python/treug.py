# Треугольник тип
import sys
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if (a + b < c) or (a + c < b) or (c+ b < a):
	print("Такого треугольника не сущствует")
	sys.exit(0)

if (a == b == c):
	print("Треугольник равносторонний")
elif (a != b) and (a != c) and (c != b):
	print("Треугольник разносторонний")
else:
	print("Треугольник равнобедренный")
