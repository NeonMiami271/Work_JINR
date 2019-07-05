
studs = list()
balls = list()
N = 100
sum = 0
k = 0
for i in range(0,N):

	name = str(input("ВВедите фамилию студента: "))
	if name == '0':
		break
	studs.append(name)
	k = k + 1
	marks = int(input("ВВедите его балл: "))
	balls.append(marks)
	sum = sum + balls[i]
	

D = sum/k

print("У следующих студентов бал выше проходного " + str("%.2d" % D) + str(":"))

for i in range(0,k):
	if (balls[i] >= D):
		print(studs[i])
