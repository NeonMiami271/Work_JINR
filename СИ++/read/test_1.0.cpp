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

void test()
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
float size = 1023;
float dream = 0;
float summa = 0;
int k;

while (!feof(input))
{	
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
				printf("Stroka_1: %d\n", k);
				C001_time = new float [size];
				fread(&number, 4, 1, input);
				
				for (int i = 0; i < size; i++)
				{
					fread(&number, 4, 1, input);
					dream = value(number);
					summa = summa + dream;
					C001_time[i] = summa;
				}
	
			}
		}
	}

}
}
