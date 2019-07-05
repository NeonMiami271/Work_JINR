f = open ('test.txt')

for line in f:
	buf = list()
	buf = line.split('_')
print(str(buf))
print(str(float(buf[3])))
