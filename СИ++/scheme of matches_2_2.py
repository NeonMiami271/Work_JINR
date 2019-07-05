# -*- coding: utf-8 -*-
import math
import random
import pylab
import tkinter
from matplotlib import mlab
from numpy.random import poisson as poi

random.seed()

#t_base=60 
m=100 #Интервал
t0=50 #Интервал в котором ищем совпадение
n=7 #Количество генерируемых шумов 
k1=poi(1, n) 
k2=poi(1, n) 




count0=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0

count_0=0
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
count_7=0
count_8=0
count_9=0
count_10=0


p=n-1
while p>=0:
	
	if k1[p]==0:
		count0+=1
		p-=1

	if k1[p]==1:
		count1+=1
		p-=1

	if k1[p]==2:
		count2+=1
		p-=1

	if k1[p]==3:
		count3+=1	
		p-=1

	if k1[p]==4:
		count4+=1		
		p-=1

	if k1[p]==5:
		count5+=1	
		p-=1

	if k1[p]==6:
		count6+=1
		p-=1

	if k1[p]==7:
		count7+=1
		p-=1

	if k1[p]==8:
		count8+=1
		p-=1

	if k1[p]==9:
		count9+=1	
		p-=1

	if k1[p]==10:
		count10+=1		
		p-=1




q=n-1
while q>=0:
	
	if k2[q]==0:
		count_0+=1
		q-=1

	if k2[q]==1:
		count_1+=1
		q-=1

	if k2[q]==2:
		count_2+=1
		q-=1

	if k2[q]==3:
		count_3+=1	
		q-=1

	if k2[q]==4:
		count_4+=1		
		q-=1

	if k2[q]==5:
		count_5+=1	
		q-=1

	if k2[q]==6:
		count_6+=1
		q-=1

	if k2[q]==7:
		count_7+=1
		q-=1

	if k2[q]==8:
		count_8+=1
		q-=1

	if k2[q]==9:
		count_9+=1	
		q-=1

	if k2[q]==10:
		count_10+=1		
		q-=1




xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ydata = [count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10]

y_data = [count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9, count_10]










print("Первое распределение Пуассона: "+str(k1))
print("Второе распределение Пуассона: "+str(k2))
print("--------------------------------------------")	
i_base=0
i=0
j=0
s=0
count=0
count_t=0

#for i_base in range(t_base):
for i in range(n):
	r1=[]
	r2=[]
	for j in range(k1[i]):
		r1.append(random.randint(1,m))
	j=0	
	for j in range(k2[i]):
		r2.append(random.randint(1,m))

	r1.sort()
	r2.sort()
	print("Первый генератор: "+ str(r1))
	print("Второй генератор: "+ str(r2))

	
	if (k1[i]>0) and (k2[i]>0):
		k1[i]=k1[i]-1

		while k1[i]>=0:
			s=k2[i]-1
			while s>=0:
				if (r1[k1[i]] - r2[s] >=0 ) and (r1[k1[i]] - r2[s] <= t0 ):
					count+=1
					count_t+=1
				
				if (- r1[k1[i]] + r2[s] >=0 ) and (- r1[k1[i]] + r2[s] <= t0 ):
					count+=1
					count_t+=1
				s=s-1

			k1[i]=k1[i]-1
	print("Число совпадений в шаге: "+str(count_t))
	count_t=0		
	print("--------------------------------------------")	
print("--------------------------------------------")	
print("--------------------------------------------")		
print("Общее число совпадений: "+ str(count))
print("--------------------------------------------")	
print("--------------------------------------------")	









pylab.title('First generator')
pylab.bar (xdata, ydata)
pylab.show()


pylab.title('Second generator')
pylab.bar (xdata, y_data)
pylab.show()
