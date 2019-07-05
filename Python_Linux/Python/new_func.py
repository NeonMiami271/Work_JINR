from ROOT import TCanvas, TH1F, TSlider
from ROOT import gROOT, gBenchmark, gRandom, TF1
import ROOT
import random 

# Create a new canvas, and customize it.
c1 = TCanvas( 'c1', 'Chi square', 200, 10, 1200, 800 )
c1.SetGrid();

histo = TH1F( 'Results', 'Chisquare', 100, -0.5, 99.5 )
histo_gauss = TH1F( 'Results', 'Gauss', 20, 100 + 0.5, -100 - 0.5 )


func = ROOT.TF1("func","gaus",-100, 100 )



histo.SetMarkerStyle( 21 )
histo.SetMarkerSize( 0.7 )

numb_iterac = 1000
numb_iterac_cycle = 1000

c1.Divide(2,1)


for i in range(numb_iterac):
	
	histo_gauss.Reset()

	for j in range(numb_iterac_cycle):
		x = random.gauss(0,1)
		histo_gauss.Fill(x)

	c1.cd(1)
	histo_gauss.Draw()
	c1.Update()

	histo_gauss.Fit(func, "Q")
	#histo_gauss.GetFit("gaus")
	x = func.GetChisquare()
	print(str(x))

	histo.Fill(x)
	c1.cd(2)
	histo.Draw()
	c1.Update()
	

c1.Update()

	