n = int(input("Какую сумму берете в кредит? "))
y = int(input("На сколько лет берете кредит? "))
p = float(input("Какой процент по кредиту за год? "))

p = p/100
m = (n*p*((1+p)**y))/(12*(((1+p)**y)-1))
s = (m*12)*y
print("Выплата должна составить " + str("%.2f" % s) + " рублей(я)") 
print("В месяц нужно выплачивать: " + str("%.2f" % (s/(y*12))) + " рублей(я)") 
input("Программа завершена.")