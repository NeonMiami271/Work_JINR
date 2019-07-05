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

void test_1_0()
{
FILE *input = NULL;
input = fopen("LAr_U47i0V_Muon_GATE_01", "rb");

if (input == NULL) 
{
	printf("Error opening file");
   	fclose(input);
}

else printf("File open!\n");

int number = 0;
float *C001_time;
float *C002_time;
float *C003_time;
float *C004_time;
int size = 1023;
float dream = 0;
float summa = 0;
int k;
float **C001_ehdr;
int count_С001 = 0;
float **C002_ehdr;
int count_С002 = 0;

while (!feof(input)) //Сколько раз встречается в файле C001
{
	fread(&number, 4, 1, input);
	if (number == 825241667)
	{
		count_С001 = count_С001 + 1;
	}
}
printf("Count_C001: %d\n", count_С001);
fseek(input, 4, SEEK_SET);

while (!feof(input)) //Сколько раз встречается в файле C001
{
	fread(&number, 4, 1, input);
	if (number == 842018883)
	{
		count_С002 = count_С002 + 1;
	}
}
printf("Count_C002: %d\n", count_С002);
fseek(input, 4, SEEK_SET);

C001_ehdr = (float**)malloc(count_С001 *sizeof(float*));

while (!feof(input))
{	
	number = 0;
	fread(&number, 4, 1, input);
	
	if (number == 1162692948) //Если встречаем Time
	{	
		k = ftell(input);
		printf("Stroka_TIME: %d\n", k);
		
		while (number != 1380206661) //Пока не дойдет до EHDR
		{	
			fread(&number, 4, 1, input);
			
			if (number == 825241667) //Временной канал C001
			{	
				k = ftell(input);
				printf("Stroka_C001: %d\n", k);
				C001_time = new float [size];
				summa = 0;
				fread(&number, 4, 1, input);
				
				for (int i = 0; i < size; i++)
				{
					fread(&number, 4, 1, input);
					dream = value(number);
					summa = summa + dream;
					C001_time[i] = summa;
				}
	
			}

			if (number == 842018883) //Временной канал C002
			{	
				k = ftell(input);
				printf("Stroka_C002: %d\n", k);
				C002_time = new float [size];
				summa = 0;
				fread(&number, 4, 1, input);
				
				for (int i = 0; i < size; i++)
				{
					fread(&number, 4, 1, input);
					dream = value(number);
					summa = summa + dream;
					C002_time[i] = summa;
				}
	
			}

			if (number == 858796099) //Временной канал C003
			{	
				k = ftell(input);
				printf("Stroka_C003: %d\n", k);
				C003_time = new float [size];
				summa = 0;
				fread(&number, 4, 1, input);
				
				for (int i = 0; i < size; i++)
				{
					fread(&number, 4, 1, input);
					dream = value(number);
					summa = summa + dream;
					C003_time[i] = summa;
				}
			}

			if (number == 875573315) //Временной канал C004
			{	
				k = ftell(input);
				printf("Stroka_C004: %d\n", k);
				C004_time = new float [size];
				summa = 0;
				fread(&number, 4, 1, input);
				
				for (int i = 0; i < size; i++)
				{
					fread(&number, 4, 1, input);
					dream = value(number);
					summa = summa + dream;
					C004_time[i] = summa;
				}
	
			}
		}
	}

	int j = 0;

	if (number == 1380206661) //Добрались до EHDR
	{
		k = ftell(input);
		printf("Stroka_EHDR: %d\n", k);

		while (!feof(input))
		{
			number = 0;
			fread(&number, 4, 1, input);
			
			if (number == 825241667) //EHDR канал C001 
			{	
				printf("j: %d\n", j);
				j = j + 1;
				k = ftell(input);
				printf("EHDR_C001: %d\n", k);
				
				
				fread(&number, 4, 1, input);

					C001_ehdr[j] = (float*)malloc(size * sizeof(float));
					for (int i = 0; i < size; i++)
					{
						number = 0;
						dream = 0;
						fread(&number, 2, 1, input);
						dream = float(number)/65535 - 0.5;
						C001_ehdr[j][i] = dream;
					}
				
			}
		}
	}
}

/*printf("C001_time\n");
for (int i = 0; i < size; i++)
{	
	printf("%f\n", C001_time[i]);
}*/

/*printf("C002_time\n");
for (int i = 0; i < size; i++)
{	
	printf("%f\n", C002_time[i]);
}*/

/*printf("C003_time\n");
for (int i = 0; i < size; i++)
{	
	printf("%f\n", C003_time[i]);
}*/

/*printf("C004_time\n");
for (int i = 0; i < size; i++)
{	
	printf("%f\n", C004_time[i]);
}*/

printf("C001_EHDR[1][i]\n");
for (int i = 0; i < size; i++)
{	
	printf("%f\n", C001_ehdr[1][i]);
}


TGraph *tgraph = new TGraph(size, C001_time, C001_ehdr[1]); // data: x,y N points 
TCanvas *tcanvas = new TCanvas("tcanvas","С002", 200, 10, 800, 600); 
tgraph->SetMarkerColor(kBlue); 
//tgraph->SetMarkerStyle(2); 
tgraph->Draw(); 
tcanvas->Update(); 

}
