from __future__ import print_function
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from array import array
import math

c1 = TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
#c1.SetFillColor( 42 )
#exit()c1.SetGrid()
ox, oy = array( 'd' ), array( 'd' )

a = 5
x = -5
step = 0.001



while x<10:

	f = x ** (2/3) + 0.9*((3.3 - (x ** 2)) ** (1/2)) * math.sin(a*math.pi*x)
	#print(str(x) + "  " + str(f))
	ox.append(x)
	oy.append(f)
	x = x + step

n = len(ox)

gr = TGraph( n, ox, oy )
gr.SetLineColor( 2 )
gr.SetLineWidth( 4 )

gr.SetMarkerColor( 4 )
#gr.SetMarkerStyle( 21 )

gr.Draw( 'AP' )
#gr.GetYaxis().SetRangeUser(0.1,2.1)
c1.SetGrid()
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()
#c1.GetFrame().SetBorderSize( 12 )
#c1.Modified()
c1.Update()