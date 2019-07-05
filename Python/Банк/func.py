def bank(a, year, per):

	i = 1
	while i<=year:
		x = a*(per/100)
		a = a + x
		i = i + 1
	return print("За " +str(year)+" лет сумма составит: "
		+str(a)+" руб.")