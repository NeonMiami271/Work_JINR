with open('test.txt') as my_file:
    data = []
    for line in my_file:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            data.append(line)

	
print(str(data) + "\n")
#print(str(len(data)))
for i in range(0,len(data)):
	for j in range(0,len(data[i])):
		data[i][j] = data[i][j] + 1

print(data)


my_file.close()


