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

numb_iterac_cycle = 10000

for i in range (numb_iterac_cycle):
	gen_buffer.append(1)


for i in range (numb_iterac):

	gen = list()
	
	for j in range(numb_iterac_cycle):
		x = random.gauss(0,1)
		gen.append(x)

	for j in range(numb_iterac_cycle):
		gen_buffer[j] = gen_buffer[j] + gen[j]

for j in range(numb_iterac_cycle):
	histo.Fill(gen_buffer[j])

print(str(len(gen_buffer)))

histo.Draw()
c1.Update()
