# -*- coding: utf-8 -*-
#import math
import random
import pylab
	

import Tkinter 
from matplotlib import mlab

random.seed()

n = 4000
hits = 0  

for i in range(0,n):
  x = random.uniform(-1,1)
  y = random.uniform(-1,1)


  if x**2+y**2 <= 1:
    hits = hits + 1
    pylab.scatter(x,y,s=5,alpha=1)


z = 4*(float(hits)/n)


print("Из "+str(n)+" событий попали " + str(hits))   
print("Число Пи приближенно равно: " + str(z))
pylab.show()
