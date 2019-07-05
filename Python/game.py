import random

print("В каком диапозоне играем?")
a = int(input("Начальное значение: "))
b = int(input("Конечное значение: "))
comp = random.randint(a,b)
#print(comp)
hum = -1
n = 0
print("Угадай число от " + str(a) + " до " + str(b))
while comp != hum:
	#if n == 5:
	#	print("Уже почти все!!!")
	hum = int(input("Число! "))
	n = n + 1
	if comp > hum:
		print ("Больше")
	elif comp < hum:
		print ("Меньше")
	else:
		print("-------------------------------------")
		print ("Ты угадал! Это число " + str(comp))
		#break
print("На разгадку понадобилось " + str(n) + " хода(ов)")

c = input("Программа завершена!")