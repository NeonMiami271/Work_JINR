x = int(input("ВВедите число: "))
k = x
n = 0
max = 0
while x>0:
	m = x % 10
	x = x // 10
	if m > max:
		max = m
		
print("Максимальная чифра в числе " + str(k) + " это " + str(max))