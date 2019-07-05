import requests, bs4
	
def vvod():
	
	while True:
		city = str(input("\nВ каком городе вы хотите узнать погоду: "))
		s = requests.get('https://sinoptik.com.ru/погода-' + city)
		b = bs4.BeautifulSoup(s.text, "html.parser")

		if str(s) == "<Response [404]>":
			if city == '':
				print("Вы ввели пустой запрос!")
			else:	
				print("Вы неверно ввели город!")
		if (city != "") and (str(s) != "<Response [404]>"):
			break
	return b


def pogoda(b):
	
	
	p=b.select('.rSide .description')
	pogoda=p[0].getText()

	p1=b.select('.temperature .p1')
	pogoda1=p1[0].getText()
	p2=b.select('.temperature .p2')
	pogoda2=p2[0].getText()

	p3=b.select('.temperature .p3')
	pogoda3=p3[0].getText()
	p4=b.select('.temperature .p4')
	pogoda4=p4[0].getText()

	p5=b.select('.temperature .p5')
	pogoda5=p5[0].getText()
	p6=b.select('.temperature .p6')
	pogoda6=p6[0].getText()

	p7=b.select('.temperature .p7')
	pogoda7=p7[0].getText()
	p8=b.select('.temperature .p8')
	pogoda8=p8[0].getText()


	print("***********************")
	
	print('Утром : ' + pogoda3 + ' ' + pogoda4)
	print('Днём : ' + pogoda5 + ' ' + pogoda6)
	print('Вечером : ' + pogoda7 + ' ' + pogoda8)
	print('Ночью : ' + pogoda1 + ' ' + pogoda2)
	
	print("***********************")
	print(pogoda.strip())
	print("\n")
	p=b.select('.rSide .description')
	pogoda=p[0].getText()
	#print(pogoda.strip())
	


#if __name__ == "__main__":
pogoda(vvod())
 