from __future__ import print_function
from ROOT import TCanvas, TGraph
from ROOT import gROOT
from math import sin
from array import array
import ROOT
c1 = TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
#c1.SetFillColor( 42 )
#exit()c1.SetGrid()
x, y = array( 'd' ), array( 'd' )

z = [52.6
,52.65
,52.7
,52.75
,52.8
,52.85
,52.9
,52.95
,53
,53.05
,53.1
,53.15
,53.2
,53.25
,53.3
,53.35
,53.4
,53.45
,53.5
,53.55
,53.6
,53.65
,53.7
,53.75
,53.8
,53.85
,53.9
,53.95
,54
,54.05
,54.1
,54.15
,54.2
,54.25
,54.3
,54.35
,54.4
,54.45
,54.5
,54.55
,54.6
,54.65
,54.7
,54.75
,54.8
,54.85
,54.9
,54.95
,55
,55.05
,55.1
,55.15
,55.2
,55.25
]

w = [0.526316
,0.512821
,0.5
,0.487805
,0.47619
,2.12766
,1.568627
,3
,3.561644
,3.956044
,4.576271
,5.432099
,5.205479
,5.051195
,4.659686
,4.471545
,4
,3.687003
,3.244444
,3.050847
,2.731707
,2.590234
,2.3375
,2.222222
,2.089552
,1.867388
,1.60166
,2.001494
,1.695147
,1.568504
,1.476079
,1.369565
,1.272265
,1.285714
,1.275078
,1.178939
,1.24336
,1.104089
,1.089631
,1.033333
,1.042654
,1.01949
,0.915594
,1.031208
,0.956072
,0.817844
,0.785714
,0.821918
,0.726073
,0.822785
,0.770791
,0.760976
,0.660377
,0.621572
]

n = len(z)


for i in range( n ):
   x.append( z[i]-0.15 )
   y.append( 1/w[i] )
   print(' i %i %f %f ' % (i,x[i],y[i]))
gr = TGraph( n, x, y )
#gr.SetLineColor( 2 )
#gr.SetLineWidth( 4 )

gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )

gr.SetTitle("")
gr.GetXaxis().SetTitle( 'Voltage, V' )
gr.GetYaxis().SetTitle( 'Inverse Logarithmic Derivative' )
gr.Draw( 'AP' )
gr.GetYaxis().SetRangeUser(0.1,2.1)
c1.SetGrid()
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()
#c1.GetFrame().SetBorderSize( 12 )
#c1.Modified()
c1.Update()

print(str(x))

print(str(y))