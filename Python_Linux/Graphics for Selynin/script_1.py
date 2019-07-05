from ROOT import *
from array import *

c1 = TCanvas( 'c1', 'Noise(threshold)', 800, 10, 1500, 1000 )
x, y = array( 'f' ), array( 'f' )

c1.SetGrid()

f = open('data.txt')

for line in f:
	buf = list()
	buf = line.split()
	x.append(float(buf[4]))
	y.append(float(buf[6]))

	n = len(x)
	gr = TGraph( n, x, y )
	gr.SetTitle("")
	gr.GetXaxis().SetTitle( 'Threshold, V' )
	gr.GetYaxis().SetTitle( 'Noise, Hz' )
	gr.SetMarkerStyle( 3 )
	gr.SetMarkerColor( 4 )
	gr.Draw( 'AP' )
	c1.Update()

#c1.Update()
#legend = TLegend(0.1,0.7,0.48,0.9,"legend")
#legend.AddEntry(gr, "Legend GR", "p")
#legend.Draw()
c1.Update()

print("Program completed!")

