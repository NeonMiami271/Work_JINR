
//#include <stdio>
//#include <io.h>
//#include <fcntl.h>
//#include <stdlib.h>
//#include <iostream>
//using namespace std;
void read()
{
FILE *input = NULL;
int number = 0;
input = fopen("LAr_U47i0V_Muon_GATE_01", "rb");

if (input == NULL) 
	{
   		printf("Error opening file");
    	fclose(input);
	}

int *C001;
float *C002;
float *C003;
float *C004;

int size_C00_ = 1024;
int k = 0;

int flag = 0;

int sign_0 = 0x80000000;
int sign_1 = 0;

int fraction_0 = 1111111;
int fraction_1 = 0;

int exponent_0 = 1111111;
int exponent_1 = 0;


while (!feof(input))
	{	
		fread(&number, 4, 1, input);
		if ((number == 825241667) && (flag == 0))
			{	
				k = ftell(input);
				printf("%d\n", k);

				C001 = new int [size_C00_];
				number = 0;
				fread(&number, 4, 1, input);
				for (int i = 0; i < size_C00_; i++)
					{
						fread(&number, 4, 1, input);
						sign_1 = number & sign_0; //Определяем знак числа из файла 

						//printf("znak: %d\n", znak_1);

						C001[i] = number;
					}
			flag=1;
			}

		/*if (number == 842018883)
			{
				C002 = new float [size_C00_];
				number = 0;
				fread(&number, sizeof(int), 1, input);
				for (int i = 0; i < size_C00_; i++)
					{
						fread(&number, sizeof(int), 1, input);
						C002[i] = number;
						
					}
			}

		if (number == 858796099)
			{
				C003 = new float [size_C00_];
				number = 0;
				fread(&number, sizeof(int), 1, input);
				for (int i = 0; i < size_C00_; i++)
					{
						fread(&number, sizeof(int), 1, input);
						C003[i] = number;
						
					}
			}

		if (number == 875573315)
			{
				C004 = new float [size_C00_];
				number = 0;
				fread(&number, sizeof(int), 1, input);
				for (int i = 0; i < size_C00_; i++)
					{
						fread(&number, sizeof(int), 1, input);
						C004[i] = number;
						
					}
			}*/
	}

fclose(input);

printf("\nC001\n");
int cik = 5;
for (int i = 0; i < cik; i++)
	{	
		printf("%d\n", C001[i]);
	}
/*printf("C002\n");
for (int i = 0; i < cik; i++)
	{	
		printf("%f\n", C002[i]);
	}
printf("C003\n");
for (int i = 0; i < cik; i++)
	{	
		printf("%f\n", C003[i]);
	}
printf("C004\n");
for (int i = 0; i < cik; i++)
	{	
		printf("%f\n", C004[i]);
	}

delete[] C001;
delete[] C002;
delete[] C003;
delete[] C004;*/
}






	