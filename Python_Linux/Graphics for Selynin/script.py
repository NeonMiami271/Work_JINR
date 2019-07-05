#from __future__ import print_function
from ROOT import *
from array import *


c1 = TCanvas( 'c1', 'Noise(threshold)', 800, 10, 1500, 1000 )
#c1.SetFillColor( 42 )
#exit()c1.SetGrid()
x, y = array( 'd' ), array( 'd' )

f = open('data.txt')


for line in f:
	probel = list()
	x1 = ''
	y1 = ''	
	for i in range(len(line)):
		if line[i] == ' ': probel.append(i)
	
	for j in range(probel[3]+1,probel[4]):
		x1 = x1 + line[j]

	for j in range(probel[5]+1,len(line)):
		y1 = y1 + line[j]

	x.append(float(x1))
	y.append(float(y1))

n = len(x)
gr = TGraph( n, x, y )
#gr.SetLineColor( 2 )
#gr.SetLineWidth( 4 )

#gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )

gr.SetTitle("")
gr.GetXaxis().SetTitle( 'Threshold, V' )
gr.GetYaxis().SetTitle( 'Noise, Hz' )
gr.Draw( 'AP' )
#gr.GetYaxis().SetRangeUser(0.1,2.1)
c1.SetGrid()
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()
#c1.GetFrame().SetBorderSize( 12 )
#c1.Modified()
c1.Update()

print("Program completed!")