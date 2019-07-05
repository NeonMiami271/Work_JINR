#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;


float float_to_time(int bite)
{
	int s = 0;
	int e = 0;
	float m = 0.0;
	float time = 0.0;
	s = ( (bite >> 31 ) == 0) ? 1 : -1;   /* Знак */
	e = ( bite >> 23 ) & 0xFF;     /* Порядок */
	for (int f = 0; f < 23; f++) 
	{
		int shift = 22 - f;
		int c = (bite >> shift) & 1;
		m += c*pow(2,(-1-f));
	}
	m+=1.0;
	time = s*m*pow(2,(e-127));

	s = 0;
	e = 0;
	m = 0.0;
	bite = 0;
	return time;			
}

//int read (int argc, char *argv[])
int read()
{
//	gROOT->Reset();
//	gROOT->Clear();	
	
FILE *file = fopen("LAr_U47i0V_Muon_GATE_01","rb");
//FILE *file = fopen(argv[1],"rb");

if (file == NULL) 
{
cout<<"Cant open file"<<endl;
return 0;
}

//cout<<sizeof(int)<<endl;
int iBite = 0;
int iBn = 0;
const int k = 1024;
int iEvent = 101;

float time_1[k];
float time_2[k];
float time_3[k];
float time_4[k];

float volt_1[k];
int volt_2[k];
int volt_3[k];
int volt_4[k];

float Average_volt_1[k];

for (int i = 0; i < k; i++)
{
	time_1[i] = 0.0;
	time_2[i] = 0.0;
	time_3[i] = 0.0;
	time_4[i] = 0.0;
	volt_1[k] = 0;
  Average_volt_1[i] = 0.0;
	volt_2[k] = 0;
	volt_3[k] = 0;
	volt_4[k] = 0;
}
int count = 0;

TH1F *ch1 = new TH1F("Ch1","Ch1",1024,0,1024);
int event = 0;

while (!feof(file))
{
	if (count == 3) break;
	fread(&iBite,4,1,file);
	if (iBite == 0x454D4954) // time header
	{

		fread(&iBite,4,1,file);
		//printf("Board # %X\n",iBite);
		printf("Board # %d\n",(iBite & 0x0000FFFF));
		fread(&iBite,4,1,file);
		printf("zdes %X\n",iBite);
		if (iBite == 0x31303043 || iBite == 0x32303043 || iBite == 0x33303043 || iBite == 0x34303043)
		{
			if (iBite == 0x31303043 ) // COO1
			{
				for (int j = 0; j < k; j++)
				{
					fread(&iBite,4,1,file);
					time_1[j] = float_to_time(iBite); // float to time converter function
					if (j>0) time_1[j] += time_1[j-1];
					iBite = 0;
					//printf("time_1[%d] = %g\n",j,time_1[j]);
				}
				
				fread(&iBite,4,1,file);
			}
			if (iBite == 0x32303043 ) // COO2
			{
				for (int j = 0; j < k; j++)
				{
					fread(&iBite,4,1,file);
					time_2[j] = float_to_time(iBite); // float to time converter function
					//printf("time_2[%d] = %g\n",j,time_2[j]);
					iBite = 0;
				}
				
				fread(&iBite,4,1,file);
			}
			if (iBite == 0x33303043 )// COO3
			{
				for (int j = 0; j < k; j++)
				{
					fread(&iBite,4,1,file);
					time_3[j] = float_to_time(iBite); // float to time converter function
					//printf("time_3[%d] = %g\n",j,time_3[j]);
					iBite = 0;
				}
				
				fread(&iBite,4,1,file);
			}
			if (iBite == 0x34303043 )// COO4
			{
				for (int j = 0; j < k; j++)
				{
					fread(&iBite,4,1,file);
					//time_4[j] = iBite;
					time_4[j] = float_to_time(iBite); // float to time converter function
					iBite = 0;
					//printf("time_4[%d] = %g\n",j,time_4[j]);
				}
				
				fread(&iBite,4,1,file);
			}
			//if (0x52444845) // Event header

		//break;
		}
	}

	while (iBite == 0x52444845) // EHDR event header
	{
		
		//printf("Event Header \n");
		fread(&iBite,4,1,file);
		event = iBite;
		//printf("Event serial number = %d \n", event);
		fread(&iBite,4,1,file);
		int year = (iBite & 0xFFFF);
		//printf("Year = %d \n", year);
		int month = (iBite >> 16) & 0xFFFF;
		//printf("Month = %d \n", month);
		fread(&iBite,4,1,file);
		int day = (iBite & 0xFFFF);
		//printf("Day = %d \n", day);
		int hour = (iBite >> 16) & 0xFFFF;
		//printf("Hour = %d \n", hour);
		fread(&iBite,4,1,file);
		int minute= (iBite & 0xFFFF);
		//printf("Minute = %d \n", minute);
		int second = (iBite >> 16) & 0xFFFF;
		//printf("Second = %d \n", second);
		fread(&iBite,4,1,file);
		int msec = (iBite & 0xFFFF);
		//printf("msec = %d \n", msec);
		int range = (iBite >> 16) & 0xFFFF;
		//printf("Range = %d mV \n", range);
		fread(&iBite,4,1,file);
		int brd = (iBite >> 16) & 0xFFFF;
		//printf("brd = %d \n", brd);
		fread(&iBite,4,1,file);
		int trg = (iBite >> 16) & 0xFFFF;
		//printf("trg = %d \n", trg);
		fread(&iBite,4,1,file);

		if (iBite == 0x31303043 ) // COO1
		{
			fread(&iBite,4,1,file);
			int scaler_1 = iBite;
			//printf("scaler_1 = %d \n", scaler_1);
			//printf("sizeof(short int) = %d\n",sizeof(unsigned short int));
			int l = 0;
			for (int j = 0; j < k/2; j++)
			{
				fread(&iBite,4,1,file);
				//time_4[j] = iBite;
				volt_1[l] = ((iBite & 0xFFFF)*pow(2,-16)-0.5)*1000;
				//printf("volt_1[%d] = %g\n",l,volt_1[l]);
				l++;
				volt_1[l] = (((iBite >> 16) & 0xFFFF)*pow(2,-16)-0.5)*1000;
				//printf("volt_1[%d] = %g\n",l,volt_1[l]);
				l++;	
				iBite = 0;
			}
      for (int i = 0; i < k; i++)
      {
        Average_volt_1[i] += volt_1[i];
      }
				fread(&iBite,4,1,file);
				if (event == 323) 
        {
          for (int d = 0; d < k; d++) Average_volt_1[d]/=323;
          TGraph *gr1 = new TGraph(k,time_1,Average_volt_1);gr1->Draw("APL");
          gr1->GetYaxis()->SetTitle("Voltage, V");
          gr1->GetYaxis()->SetTitleOffset(1.5);
          gr1->GetXaxis()->SetTitle("time, ns");
        }
		}

		if (iBite == 0x32303043 ) // COO2
		{
			fread(&iBite,4,1,file);
			int scaler_2 = iBite;
			//printf("scaler_2 = %d \n", scaler_2);
			//printf("sizeof(short int) = %d\n",sizeof(unsigned short int));
			int l = 0;
			for (int j = 0; j < k/2; j++)
			{
				fread(&iBite,4,1,file);
				//time_4[j] = iBite;
				volt_2[l] = iBite & 0xFFFF;
				//printf("volt_1[%d] = %d\n",l,volt_1[l]);
				l++;
				volt_2[l] = (iBite >> 16) & 0xFFFF;
				//printf("volt_2[%d] = %d\n",l,volt_2[l]);
				l++;	
				iBite = 0;
			}
				fread(&iBite,4,1,file);
		}
		if (iBite == 0x33303043 ) // COO3
		{
			fread(&iBite,4,1,file);
			int scaler_3 = iBite;
			//printf("scaler_3 = %d \n", scaler_3);
			//printf("sizeof(short int) = %d\n",sizeof(unsigned short int));
			int l = 0;
			for (int j = 0; j < k/2; j++)
			{
				fread(&iBite,4,1,file);
				//time_4[j] = iBite;
				volt_3[l] = iBite & 0xFFFF;
				//printf("volt_3[%d] = %d\n",l,volt_3[l]);
				l++;
				volt_3[l] = (iBite >> 16) & 0xFFFF;
				//printf("volt_3[%d] = %d\n",l,volt_3[l]);
				l++;	
				iBite = 0;
			}
				fread(&iBite,4,1,file);
		}
		if (iBite == 0x34303043 ) // COO4
		{
			fread(&iBite,4,1,file);
			int scaler_4 = iBite;
			//printf("scaler_4 = %d \n", scaler_4);
			//printf("sizeof(short int) = %d\n",sizeof(unsigned short int));
			int l = 0;
			for (int j = 0; j < k/2; j++)
			{
				fread(&iBite,4,1,file);
				//time_4[j] = iBite;
				volt_4[l] = iBite & 0xFFFF;
				//printf("volt_4[%d] = %d\n",l,volt_4[l]);
				l++;
				volt_4[l] = (iBite >> 16) & 0xFFFF;
				//printf("volt_4[%d] = %d\n",l,volt_4[l]);
				l++;	
				iBite = 0;
			}
				fread(&iBite,4,1,file);
		}
	//	event++;
	}
	printf("iBite = %X\n",iBite);
	//printf("Pos = %d\n",ftell(file));
//	printf("Event = %d", event);
	count++;
	//break;
}

return 0;
}


