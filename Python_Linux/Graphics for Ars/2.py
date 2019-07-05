from __future__ import print_function
from ROOT import TCanvas, TGraph, TGraphErrors
from ROOT import gROOT
from math import sin
from array import array
import math
c1 = TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
cv = TCanvas( 'cv', 'A Simple Graph Example', 200, 10, 700, 500 )
#c1.SetFillColor( 42 )
#exit()c1.SetGrid()
x22, y22 = array( 'd' ), array( 'd' )
x53, y53 = array( 'd' ), array( 'd' )

xv22, yv22 = array( 'd' ), array( 'd' )
xv53, yv53 = array( 'd' ), array( 'd' )

xe22, ye22 = array( 'd' ), array( 'd' )
xe53, ye53 = array( 'd' ), array( 'd' )

xp22, yp22 = array( 'd' ), array( 'd' )
xp53, yp53 = array( 'd' ), array( 'd' )



z22 = [
0.5
,1.0
,1.5
,1.7
,1.7
,2
,2
,2
,2.5
,3
,3.5
,4
,4.5
]

z53 = [
0.5
,1.0
,1.5
,2
,2
,2
,2.5
,3
,3.5
,4
,4.5
]

w22 = [
0.6
,1.207
,1.56
,1.65
,1.63
,1.84
,1.81
,1.82
,2.05
,2.21
,2.35
,2.45
,2.49
]

w53 = [
0.62
,1.24
,1.63
,1.92
,1.93
,1.89
,2.16
,2.3
,2.44
,2.62
,2.64
]

n22 = len(z22)
n53 = len(z53)



for i in range( n22 ):
   x22.append( z22[i] )
   xv22.append( z22[i]+26.6 )

   y22.append( w22[i] )
   yv22.append( w22[i] )
   xe22.append( 0 )
   ye22.append( w22[i]*(1/math.sqrt(30000)) * (math.sqrt(math.exp((w22[i]-1))/(w22[i]*w22[i])) ))
 
   #print(' i %i %f %f ' % (i,x[i],y[i]))
gr22 = TGraphErrors( n22, x22, y22, xe22, ye22 )
grv22 = TGraph( n22, xv22, yv22 )


for i in range( n53 ):
   x53.append( z53[i] )
   xv53.append( z53[i] + 24.62 )
   y53.append( w53[i] )
   yv53.append( w53[i] )
   xe53.append( 0 )
   ye53.append( w53[i] )

   #print(' i %i %f %f ' % (i,x1[i],y1[i]))
xv53.append( 32 )
yv53.append( -1 )

gr53 = TGraph( n53, x53, y53 )
grv53 = TGraph( n53 + 1, xv53, yv53 )


print(str(x22))
print(str(y22))
print(str(x53))
print(str(y53))
print(str(ye22))
print(str(xv22))
print(str(xv53))
print(str(yv53))

#gr.SetLineColor( 2 )
#gr.SetLineWidth( 4 )

gr22.SetMarkerColor( 2 )
gr22.SetMarkerStyle( 21 )

gr53.SetMarkerColor( 4 )
gr53.SetMarkerStyle( 20 )

gr22.SetTitle("")
gr22.GetXaxis().SetTitle( 'Overvoltage, V' )
gr22.GetYaxis().SetTitle( 'Efficiency, ph.e.' )
gr22.GetYaxis().SetRangeUser( 0, 3 )

c1.cd()
gr22.Draw( 'AP' )
gr53.Draw( 'P' )
#gr.GetYaxis().SetRangeUser(0.1,2.1)
c1.SetGrid()
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()

cv.cd()
grv53.SetTitle("")
cv.SetGrid()

grv53.GetXaxis().SetTitle( 'Voltage, V' )
grv53.GetYaxis().SetTitle( 'Efficiency, ph.e.' )

grv22.SetMarkerColor( 2 )
grv22.SetMarkerStyle( 21 )

grv53.SetMarkerColor( 4 )
grv53.SetMarkerStyle( 20 )

grv53.Draw( 'AP' )
grv22.Draw( 'P' )
grv53.GetYaxis().SetRangeUser( 0, 3 )
grv53.GetXaxis().SetRangeUser( 0, 32 )
cv.Update()
#c1.GetFrame().SetBorderSize( 12 )
#c1.Modified()
