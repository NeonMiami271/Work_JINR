import math

a = 7
x = -5
step = 0.1

ox = list()
oy = list()

while x<5:

	f = x ** (2/3) + 0.9*((3.3 - (x ** 2)) ** (1/2)) * math.sin(a*math.pi*x)
	print(str(x) + "  " + str(f))
	ox.append(x)
	oy.append(f)
	x = x + step