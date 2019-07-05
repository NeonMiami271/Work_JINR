from ROOT import TCanvas, TH1F, TSlider
from ROOT import gROOT, gBenchmark, gRandom
import random 

# Create a new canvas, and customize it.
c1 = TCanvas( 'c1', 'The HSUM example', 200, 10, 600, 400 )
c1.SetGrid();


# Create some histograms.
histo_1  = TH1F( 'total', 'Generator multiplication 1 & 2', 1000, -100, 100 )
histo_2  = TH1F( 'total', 'Generator multiplication 1 & 2 & 3', 1000, -1000, 1000 )
histo_3  = TH1F( 'total', 'Generator multiplication 1 & 2 & 3 & 4', 1000, -10000, 10000 )
histo_4  = TH1F( 'total', 'Generator multiplication 1 & 2 & 3 & 4 & 5', 1000, -100000, 100000 )

histo_gen  = TH1F( 'total', 'Generator first', 1000, -15, 15 )


# Set canvas/frame attributes.
histo_1.SetMarkerStyle( 21 )
histo_1.SetMarkerSize( 0.7 )
histo_2.SetMarkerStyle( 21 )
histo_2.SetMarkerSize( 0.7 )
histo_3.SetMarkerStyle( 21 )
histo_3.SetMarkerSize( 0.7 )
histo_4.SetMarkerStyle( 21 )
histo_4.SetMarkerSize( 0.7 )

gen_1 = list()
gen_2 = list()
gen_3 = list()
gen_4 = list()
gen_5 = list()

numb_iterac = 100000
a = -10
b = 10

for i in range(0,numb_iterac):
	x = random.randint(a,b)
	histo_gen.Fill(x)
	gen_1.append(x)


for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_2.append(x)


for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_3.append(x)


for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_4.append(x)

for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_5.append(x)


mul_1 = list()
for i in range(0,numb_iterac):
	x = gen_1[i] * gen_2[i]
	#print(str(x))
	histo_1.Fill(x)
	mul_1.append(x)

mul_2 = list()
for i in range(0,numb_iterac):
	x = mul_1[i] * gen_3[i]
	#print(str(x))
	histo_2.Fill(x)
	mul_2.append(x)

mul_3 = list()
for i in range(0,numb_iterac):
	x = mul_2[i] * gen_4[i]
	#print(str(x))
	histo_3.Fill(x)
	mul_3.append(x)
	
for i in range(0,numb_iterac):
	x = mul_3[i] * gen_5[i]
	#print(str(x))
	histo_4.Fill(x)
	

c1.Divide(3,2)
c1.cd(1)
histo_1.Draw()
c1.cd(2)
histo_2.Draw()
c1.cd(3)
histo_3.Draw()
c1.cd(4)
histo_4.Draw()
c1.cd(5)
histo_gen.Draw()
c1.Update()


