from __future__ import print_function
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from math import sin
from array import array
c1 = TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
#c1.SetFillColor( 42 )
#exit()c1.SetGrid()
x, y = array( 'd' ), array( 'd' )
x1, y1 = array( 'd' ), array( 'd' )


z = [
24.62
,25.12
,25.62
,26.12
,26.62
,27.12
,27.62
,28.12
,28.62
,29.12
]

w = [
-1
,0.622872144730442
,1.24137300554307
,1.62857359285547
,1.912892
,2.16500413593491
,2.29539112066552
,2.44366953504207
,2.61839590996677
,2.6413704739832
]

z1 = [
24.62
,25.12
,25.62
,26.12
,26.62
,27.12
,27.62
,28.12
,28.62
,29.12
]

w1 = [
-1
,-1
,1.29
,1.65
,1.91333
,2.2
,2.31
,2.44
,2.65
,2.66
]

n = len(z)
n1 = len(z1)



for i in range( n ):
   x.append( z[i]-24.62 )
   y.append( w[i] )
   #print(' i %i %f %f ' % (i,x[i],y[i]))
gr = TGraph( n, x, y )

for i in range( n1 ):
   x1.append( z1[i]-24.62 )
   y1.append( w1[i] )
   #print(' i %i %f %f ' % (i,x1[i],y1[i]))
gr1 = TGraph( n1, x1, y1 )

print(str(x))
print(str(y))
print(str(x1))
print(str(y1))
#gr.SetLineColor( 2 )
#gr.SetLineWidth( 4 )

gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )

gr1.SetMarkerColor( 2 )
gr1.SetMarkerStyle( 20 )

gr.SetTitle("")
gr.GetXaxis().SetTitle( 'Voltage, V' )
gr.GetYaxis().SetTitle( 'Mu' )
gr.GetYaxis().SetRangeUser( 0, 3 )

gr.Draw( 'AP' )
gr1.Draw( 'P' )
#gr.GetYaxis().SetRangeUser(0.1,2.1)
c1.SetGrid()
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()
#c1.GetFrame().SetBorderSize( 12 )
#c1.Modified()

