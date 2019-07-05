float value(int number)
{
	int sign = 0;
	int exp = 0;
	float fraction = 0;
	float result = 0;

	if ((number >> 31)==0)
	{
		sign=1;
	}
	else
	{
		sign=-1;
	}

	exp = ((number>>23)&0xFF);
	for(int i=0;i<23;i++)
	{
		int j=22-i;
		int step=((number>>j) & 1);
		fraction = fraction + step*pow(2,(-1-j));
	}	

	if (fraction!=0)
	{
		fraction = fraction + 1;
	}

	result = sign*fraction*pow(2,(exp-127));
	sign = 0;
	exp = 0;
	fraction = 0;
	number = 0;
	return result;
}	

/*float value_voltage(int number)
{
	int sign = 0;
	int exp = 0;
	float fraction = 0;
	float result = 0;

	if ((number >> 15)==0)
	{
		sign=1;
	}
	else
	{
		sign=-1;
	}

	exp = ((number>>11)&0xF);
	for(int i=0;i<11;i++)
	{
		int j=10-i;
		int step=((number>>j) & 1);
		fraction = fraction + step*pow(2,(-1-j));
	}	

	if (fraction!=0)
	{
		fraction = fraction + 1;
	}

	result = sign*fraction*pow(2,(exp-63));
	sign = 0;
	exp = 0;
	fraction = 0;
	number = 0;
	return result;
}	*/

void test(){


FILE *input = NULL;

input = fopen("LAr_U47i0V_Muon_GATE_01", "rb");

if (input == NULL) 
{
	printf("Error opening file");
   	fclose(input);
}
else printf("File open!\n");

int number = 0;
float *C001;
float *C002;
float *C003;
float *C004;
float *voltage_C001;

int size_C00_ = 1023;
int k = 0;
int flag = 0;
int count = 0;
float summa_C001 = 0;
float voltage = 0;
float dream = 0;
float summa_1 = 0;

printf("********************************************************\n");

while (!feof(input))
{
	fread(&number, 4, 1, input);
	if (number == 825241667)
	{
		count = count + 1;
	}
}
printf("Count_C001: %d\n", count);
fseek(input, 4, SEEK_SET);
count = 0;
/*
while (!feof(input))
{
	fread(&number, 4, 1, input);
	if (number == 842018883)
	{
		k = ftell(input);
		printf("Stroka_Voltage_C001: %d\n", k);
	}
}
printf("Count_C002: %d\n", count);
fseek(input, 4, SEEK_SET);
count = 0;

while (!feof(input))
{
	fread(&number, 4, 1, input);
	if (number == 858796099)
	{
		count = count + 1;
	}
}
printf("Count_C003: %d\n", count);
fseek(input, 4, SEEK_SET);
count = 0;

while (!feof(input))
{
	fread(&number, 4, 1, input);
	if (number == 875573315)
	{
		count = count + 1;
	}
}
printf("Count_C004: %d\n", count);
fseek(input, 4, SEEK_SET);*/

while (!feof(input))
{	
	//printf("flag: %d\n", flag);
	//printf("In cycle!\n");
	number = 0;
	fread(&number, 4, 1, input);
	
	if ((number == 825241667) && (flag == 0))
	{	
		k = ftell(input);
		printf("Stroka_1: %d\n", k);
		C001 = new float [size_C00_];
		fread(&number, 4, 1, input);
		for (int i = 0; i < size_C00_; i++)
		{
			fread(&number, 4, 1, input);
			dream = value(number);
			summa_1 = summa_1 + dream;
			C001[i] = summa_1;
		}
	flag = flag + 1;
	}

	if ((number == 842018883) && (flag == 1))
	{	
		k = ftell(input);
		printf("Stroka_2: %d\n", k);
		C002 = new float [size_C00_];
		fread(&number, 4, 1, input);
		for (int i = 0; i < size_C00_; i++)
		{
			fread(&number, 4, 1, input);
			C002[i] = value(number);
		}
	flag = flag + 1;
	}

	if ((number == 858796099) && (flag == 2))
	{	
		k = ftell(input);
		printf("Stroka_3: %d\n", k);
		C003 = new float [size_C00_];
		fread(&number, 4, 1, input);
		for (int i = 0; i < size_C00_; i++)
		{
			fread(&number, 4, 1, input);
			C003[i] = value(number);
		}
	flag = flag + 1;
	}

	if ((number == 875573315) && (flag == 3))
	{	
		k = ftell(input);
		printf("Stroka_4: %d\n", k);
		C004 = new float [size_C00_];
		fread(&number, 4, 1, input);
		for (int i = 0; i < size_C00_; i++)
		{
			fread(&number, 4, 1, input);
			C004[i] = value(number);
		}
	flag = flag + 1;
	}

	if (number == 825241667) //Header events C001
	{	
		k = ftell(input);
		printf("Stroka_Voltage_C001: %d\n", k);
		voltage_C001 = new float [size_C00_];
		for (int i = 0; i < size_C00_; i++)
		{	
			number = 0;
			voltage = 0;
			fread(&number, 2, 1, input);
			//printf("number: %d\n", number);
			voltage = float(number)/65535 - 0.5;
			voltage_C001[i] = voltage;
			printf("voltage_C001: %f\n", voltage);
		}  
	}
}


fclose(input);
printf("----------------------------------------------------------------------------\n");

/*printf("\nvoltage_C001\n");
for (int i = 0; i < size_C00_; i++)
{	
	printf("voltage_C001: %f\n", voltage_C001[i]);
}

//printf("Summa_C001: %f\n", summa_C001);
/*printf("\nC001\n");
for (int i = 0; i < size_C00_; i++)
{	
	printf("%f\n", C001[i]);
}

printf("C002\n");
for (int i = 0; i < size_C00_; i++)
{	
	printf("%f\n", C002[i]);
}

printf("C003\n");
for (int i = 0; i < size_C00_; i++)
{	
	printf("%f\n", C003[i]);
}

printf("C004\n");
for (int i = 0; i < size_C00_; i++)
{	
	printf("%f\n", C004[i]);
}*/

/*float summa_1 = 0;
float summa_2 = 0;
float summa_3 = 0;
float summa_4 = 0;

for (int i = 0; i < size_C00_; i++)
{	
	summa_1 = summa_1 + C001[i];
	summa_2 = summa_2 + C002[i];
	summa_3 = summa_3 + C003[i];
	summa_4 = summa_4 + C004[i];
}

printf("Summa_C001: %f\n", summa_1);
printf("Summa_C002: %f\n", summa_2);
printf("Summa_C003: %f\n", summa_3);
printf("Summa_C004: %f\n", summa_4); */

delete[] C001;
delete[] C002;
delete[] C003;
delete[] C004;
delete[] voltage_C001;

//TH1F *Histo_C001 = new TH1F ("Histo_C001", "", 100, -1, 10);
TGraph *tgraph = new TGraph(size_C00_, C001, voltage_C001); // data: x,y N points 
TCanvas *tcanvas = new TCanvas("tcanvas","С001", 200, 10, 800, 600); 
tgraph->SetMarkerColor(kBlue); 
//tgraph->SetMarkerStyle(2); 
tgraph->Draw(); 
tcanvas->Update(); 
}





