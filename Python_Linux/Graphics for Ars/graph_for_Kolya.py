#from future import print_function
from ROOT import TCanvas, TGraph, TGraphErrors, TLegend
from ROOT import gROOT
from math import sin
from array import array
import math
c1 = TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
cv = TCanvas( 'cv', 'A Simple Graph Example', 200, 10, 700, 500 )
# ci = TCanvas( 'ci', 'A Simple Graph Example', 200, 10, 700, 500 )
cd = TCanvas( 'cd', 'A Simple Graph Example', 200, 10, 700, 500 )
cdo = TCanvas( 'cdo', 'A Simple Graph Example', 200, 10, 700, 500 )
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

xi22, yi22 = array( 'd' ), array( 'd' )
xi53, yi53 = array( 'd' ), array( 'd' )

xd22, yd22 = array( 'd' ), array( 'd' )
xd53, yd53 = array( 'd' ), array( 'd' )

xdo22, ydo22 = array( 'd' ), array( 'd' )
xdo53, ydo53 = array( 'd' ), array( 'd' )

xer22, yer22 = array( 'd' ), array( 'd' )
xer53, yer53 = array( 'd' ), array( 'd' )


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

I22 = [17.5,53.5,112,141,144,195,196,198,310,475,700,795,1420]
I53 = [0.8,2.4,4.7,7.8,8.0,8.1,12.6,19.5,30.1,47.5,80.5]


zd22 = [0,1.5,1.7,1.7,2,2,2,2.5,3,3.5,4,4.5]
D22  = [0.1,578,596, 584, 670, 676, 681, 781, 879, 970, 1073, 1236]
nd22 = len(zd22)

zd53 = [2,2,2,2.5,3,3.5,4,4.5]
D53  = [ 4.5, 4.8, 5, 6.3, 8.4, 10.2, 14.1, 16.3 ]
nd53 = len(zd53)

n22 = len(z22)
n53 = len(z53)



for i in range( n22 ):
   x22.append( z22[i] )
   xv22.append( z22[i]+26.6 )

   y22.append( w22[i]  * 40 / 2.49 )
   yv22.append( w22[i] * 40 / 2.49 )
   xe22.append( 0 )
   ye22.append( w22[i] * 0.02)


for i in range( nd22 ):
   xd22.append( zd22[i] + 26.6 )
   xdo22.append( zd22[i] )
   yd22.append( D22[i] * 1000)
   xer22.append( 0 )
   yer22.append( float (w22[i]) * float(0.02) )
print("error - " + str(yer22))


   #print(' i %i %f %f ' % (i,x[i],y[i]))
gr22 = TGraphErrors( n22, x22, y22, xe22, ye22 )
grv22 = TGraphErrors( n22, xv22, yv22, xer22, yer22 )

# gri22 = TGraph( ni22, xi22, yi22 )
grd22 = TGraph( nd22, xd22, yd22 )
grdo22 = TGraph( nd22, xdo22, yd22 )


for i in range( n53 ):
   x53.append( z53[i] )
   xv53.append( z53[i] + 24.62 )
   y53.append( w53[i]  * 40 / 2.49)
   yv53.append( w53[i]  * 40 / 2.49)
   xe53.append( 0 )
   ye53.append( w53[i] )


#print(' i %i %f %f ' % (i,x1[i],y1[i]))
xv53.append( 32 )
yv53.append( -1 )


for i in range( nd53 ):
   xd53.append( zd53[i] + 24.62 )
   xdo53.append( zd53[i] )
   yd53.append( D53[i] * 1000 )



gr53 = TGraph( n53, x53, y53 )
grv53 = TGraph( n53 + 1, xv53, yv53 )

grd53 = TGraph( nd53, xd53, yd53 )
grdo53 = TGraph( nd53, xdo53, yd53 )


# print(str(x22))
# print(str(y22))
# print(str(x53))
# print(str(y53))
# print(str(ye22))
# print(str(xv22))
# print(str(xv53))
# print(str(yv53))

print(str(xd22))
print(str(yd22))
print()
print(str(xd53))
print(str(yd53))

legend = TLegend(0.666189,0.143158,0.895415,0.290526);
legend.AddEntry(gr53, "-53.0 #circC ","ep");
legend.AddEntry(gr22," 22.0 #circC ","ep");

#gr.SetLineColor( 2 )
#gr.SetLineWidth( 4 )

gr22.SetMarkerColor( 2 )
gr22.SetMarkerStyle( 21 )

gr53.SetMarkerColor( 4 )
gr53.SetMarkerStyle( 20 )

gr22.SetTitle("PDE vs Voltage")
gr22.GetXaxis().SetTitle( 'Overvoltage, V' )
gr22.GetYaxis().SetTitle( 'PDE, %' )
gr22.GetYaxis().SetRangeUser( 0, 45 )

c1.cd()
gr22.Draw( 'AP' )
gr53.Draw( 'P' )
legend.Draw();
#gr.GetYaxis().SetRangeUser(0.1,2.1)
c1.SetGrid()
# TCanvas.Update() draws the frame, after which one can change it
c1.Update()

cv.cd()
grv53.SetTitle("PDE vs Voltage")
cv.SetGrid()

grv53.GetXaxis().SetTitle( 'Voltage, V' )
grv53.GetYaxis().SetTitle( 'PDE, %' )

grv22.SetMarkerColor( 2 )
grv22.SetMarkerStyle( 21 )

grv53.SetMarkerColor( 4 )
grv53.SetMarkerStyle( 20 )

grv53.Draw( 'AP' )
grv22.Draw( 'P' )
grv53.GetYaxis().SetRangeUser( 0, 45 )
grv53.GetXaxis().SetRangeUser( 0, 31.5 )
legend.Draw();
cv.Update()
c1.Print("pde_temp_over.pdf")
cv.Print("pde_temp_volt.pdf")

# DCR
cd.cd()
grd22.SetTitle("DCR vs Voltage")
cd.SetGrid()

grd22.SetMarkerColor( 2 )
grd22.SetMarkerStyle( 21 )

grd53.SetMarkerColor( 4 )
grd53.SetMarkerStyle( 20 )


grd22.Draw( 'AP' )
grd53.Draw( 'P' )
legend.Draw();

grd22.GetXaxis().SetTitle( 'Voltage, V' )
grd22.GetYaxis().SetTitle( 'DCR, Cs' )

grd22.GetYaxis().SetRangeUser( 1000, 10000000 )
# grv22.GetXaxis().SetRangeUser( 0, 31.5 )
cd.SetLogy()
cd.Update()

# DCR Overvoltage
cdo.cd()

grdo22.SetTitle("+22 #circC")
# grdo55.SetTitle("-53 #circC")
cdo.SetGrid()

grdo22.SetMarkerColor( 2 )
grdo22.SetMarkerStyle( 21 )

grdo53.SetMarkerColor( 4 )
grdo53.SetMarkerStyle( 20 )


grdo22.Draw( 'AP' )
grdo53.Draw( 'P' )

grdo22.GetXaxis().SetTitle( 'Overvoltage, V' )
grdo22.GetYaxis().SetTitle( 'DCR, Cs' )

grdo22.GetYaxis().SetRangeUser( 1000, 10000000 )
grdo22.GetXaxis().SetRangeUser( 1, 31.5 )


legend.Draw();

grdo22.SetTitle("DCR vs Voltage")
cdo.SetLogy()
cdo.Update()

cdo.Print("dcr_temp_over.pdf")
cd.Print("dcr_temp_volt.pdf")