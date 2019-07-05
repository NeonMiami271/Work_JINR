from ROOT import TCanvas, TH1F, TSlider
from ROOT import gROOT, gBenchmark, gRandom, TF1
import ROOT
import random 
import time

# Create a new canvas, and customize it.
c1 = TCanvas( 'c1', 'Gauss distribution', 200, 10, 1600, 1400 )
c1.SetGrid();

c1.Divide(2,1)


histo = TH1F( 'Results', 'Chisquare', 100, -100, 100 )
histo_gauss = TH1F( 'Results', 'Gauss', 100, -10, 10 )


histo.SetMarkerStyle( 21 )
histo.SetMarkerSize( 0.7 )
histo_gauss.SetMarkerStyle( 21 )
histo_gauss.SetMarkerSize( 0.7 )

numb_iterac = 100
numb_iterac_cycle = 1000
for i in range(numb_iterac):
	
	histo_gauss.Reset()

	for j in range(numb_iterac_cycle):
		x = random.gauss(0,1)
		histo_gauss.Fill(x)

	c1.cd(1)
	histo_gauss.Draw()
	c1.Update()
	#time.sleep(1)

	histo_gauss.Fit("gaus")
	x = histo_gauss.Get()
	#print(str(x))
	histo.Fill(x)
	c1.cd(2)
	histo.Draw()
	c1.Update()


c1.cd(2)
histo.Draw()
c1.Update()




