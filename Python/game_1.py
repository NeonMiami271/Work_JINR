import random
a = 1
b = 100
comp = random.randint(a,b)
#print(comp)
hum = -1
n = 0
print("Угадай число от " + str(a) + " до " + str(b))
while comp != hum:
	if n == 3:
		print("Эт чё бл%ть такое?")
	if n == 5:
		print("Альфа на*уй!!!")
	hum = int(input("Число! "))
	n = n + 1
	if comp > hum:
		print ("Больше")
	elif comp < hum:
		print ("Меньше")
	else:
		print ("Красавчик!!!")
		break
print("На разгадку понадобилось " + str(n) + " хода(ов)")