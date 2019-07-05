
my_file = open("variation.txt", "w+")

#main_vector = [0, 0, 0, 1, 2, 2, 0, 4, 0, 1]
#main_vector = [0, 0, 0, 0, 2, 2, 0, 5, 0, 1]
main_vector = [0, 0, 0, 2, 0, 3, 0, 5, 0, 0]

#main_vector = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#main_vector = [1, 1, 1, 1, 1, 1, 0, 2, 1, 1]
#main_vector =  [1, 1, 1, 1, 1, 1, 0, 3, 0, 1]
#main_vector = [1, 0, 1, 1, 2, 1, 0, 3, 0, 1]
#main_vector = [0, 0, 1, 1, 2, 1, 0, 4, 0, 1]
#main_vector =  [0, 0, 1, 1, 2, 1, 0, 4, 0, 1]
for z in range(len(main_vector)):
	my_file.write(str(main_vector[z]) + " ")
my_file.write("\n")


for i in range(0, len(main_vector)):
	#double_vector = main_vector
	if (main_vector[i] > 0):

		for j in range(0, len(main_vector)):
				

			main_vector_double = list.copy(main_vector)
			#print(str(main_vector_double))
			
			#print(str(main_vector_double[i]))
			
			if (i!=j):

				main_vector_double[i] = main_vector_double[i] - 1
				main_vector_double[j] = main_vector_double[j] + 1
			
				sum = 0	
				for z in range(0,len(main_vector_double)):
					sum = sum + main_vector_double[z]
			
				if (sum == 10):	
				
					for z in range(len(main_vector_double)):
						my_file.write(str(main_vector_double[z]) + " ")
					my_file.write("\n")


				