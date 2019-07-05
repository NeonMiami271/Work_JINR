from __future__ import print_function
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from math import sin
from array import array
c1 = TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
#c1.SetFillColor( 42 )
#exit()c1.SetGrid()
x, y = array( 'd' ), array( 'd' )

z = [
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

w = [
0.6
,1.207
,1.56
,1.84
,1.81
,1.82
,2.05
,2.21
,2.35
,2.45
,2.49
]

n = len(z)


for i in range( n ):
   x.append( z[i]-0.25 )
   y.append( w[i] )
   print(' i %i %f %f ' % (i,x[i],y[i]))
gr = TGraph( n, x, y )
#gr.SetLineColor( 2 )
#gr.SetLineWidth( 4 )

gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )

gr.SetTitle("Breakdown Voltage")
gr.GetXaxis().SetTitle( 'Voltage, V' )
gr.GetYaxis().SetTitle( '(1/I)*(dI/dV)' )
gr.Draw( 'AP' )
#gr.GetYaxis().SetRangeUser(0.1,2.1)
c1.SetGrid()
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()
#c1.GetFrame().SetBorderSize( 12 )
#c1.Modified()
c1.Update()

print(str(x))

print(str(y))