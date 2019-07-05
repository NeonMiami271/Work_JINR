from ROOT import TCanvas, TH1F, TSlider
from ROOT import gROOT, gBenchmark, gRandom
import random 

# Create a new canvas, and customize it.
c1 = TCanvas( 'c1', 'The HSUM example', 200, 10, 600, 400 )
c1.SetGrid();

# Create some histograms.
histo_1  = TH1F( 'total', 'Generator amounts 1 & 2', 1000, -30, 30 )
histo_2  = TH1F( 'total', 'Generator amounts 1 & 2 & 3', 1000, -40, 40 )
histo_3  = TH1F( 'total', 'Generator amounts 1 & 2 & 3 & 4', 1000, -50, 50 )
histo_4  = TH1F( 'total', 'Generator amounts 1 & 2 & 3 & 4 & 5', 1000, -60, 60 )
histo_5 = TH1F( 'total', 'Generator amounts 1 & 2 & 3 & 4 & 5 & 6 & 7', 1000, -80, 80 )

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
gen_6 = list()
gen_7 = list()
gen_8 = list()
gen_9 = list()
gen_10 = list()

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

for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_6.append(x)

for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_7.append(x)

for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_8.append(x)

for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_9.append(x)

for i in range(0,numb_iterac):
	x = random.randint(a,b)
	gen_10.append(x)


mul_1 = list()
for i in range(0,numb_iterac):
	x = gen_1[i] + gen_2[i]
	#print(str(x))
	histo_1.Fill(x)
	mul_1.append(x)

mul_2 = list()
for i in range(0,numb_iterac):
	x = mul_1[i] + gen_3[i]
	#print(str(x))
	histo_2.Fill(x)
	mul_2.append(x)

mul_3 = list()
for i in range(0,numb_iterac):
	x = mul_2[i] + gen_4[i]
	#print(str(x))
	histo_3.Fill(x)
	mul_3.append(x)

mul_4 = list()	
for i in range(0,numb_iterac):
	x = mul_3[i] + gen_5[i]
	histo_4.Fill(x)
	mul_4.append(x)

mul_5 = list()	
for i in range(0,numb_iterac):
	x = mul_4[i] + gen_6[i]
	mul_5.append(x)

mul_6 = list()	
for i in range(0,numb_iterac):
	x = mul_5[i] + gen_7[i]
	histo_5.Fill(x)
	mul_6.append(x)

mul_7 = list()	
for i in range(0,numb_iterac):
	x = mul_6[i] + gen_8[i]
	mul_7.append(x)

mul_8 = list()	
for i in range(0,numb_iterac):
	x = mul_7[i] + gen_9[i]
	mul_8.append(x)

mul_9 = list()	
for i in range(0,numb_iterac):
	x = mul_8[i] + gen_10[i]
	histo_5.Fill(x)
	mul_9.append(x)


#c1.Divide(3,2)
#c1.cd(1)
#histo_1.Draw()
#c1.cd(2)
#histo_2.Draw()
#c1.cd(3)
#histo_3.Draw()
#c1.cd(4)
#histo_4.Draw()
#c1.cd(5)
#histo_gen.Draw()
histo_5.Draw()
c1.Update()

