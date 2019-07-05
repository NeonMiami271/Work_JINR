from ROOT import TCanvas, TH1F, TSlider
from ROOT import gROOT, gBenchmark, gRandom
import random 

# Create a new canvas, and customize it.
c1 = TCanvas( 'c1', 'Gauss distribution', 200, 10, 600, 400 )
c1.SetGrid();

numb_iterac = 100

# Create some histograms.
histo = TH1F( 'Results', 'Generator Gauss amounts', numb_iterac*10, -numb_iterac, numb_iterac )

# Set canvas/frame attributes.
histo.SetMarkerStyle( 21 )
histo.SetMarkerSize( 0.7 )


gen = list()
gen_buffer = list()

numb_iterac_cycle = 1000


for j in range(numb_iterac_cycle):
	x = random.gauss(0,1)
	histo.Fill(x)
	gen.append(x)


histo.Fit("gaus")
histo.Draw()
c1.Update()
