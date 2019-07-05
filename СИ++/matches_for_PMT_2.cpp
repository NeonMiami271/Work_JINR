
// Счетчик совпадений для окна, длительностью 200 нс. 2 генератора шума

void matches_for_PMT_2()
{

//TH1D *HistoPoisson1 = new TH1D ("HistoPoisson1", "Poisson for 1 gen", 100, -1, 10);
//TH1D *HistoPoisson2 = new TH1D ("HistoPoisson2", "Poisson for 2 gen", 100, -1, 10);
TH1D *HistoMatches = new TH1D ("HistoMatches", "General matches", 800, 350+0.5, 550+0.5);
//TH1D *HistoGenerator = new TH1D ("HistoGenerator", "First Gen", 10000, 0, 10000);


TRandom3 *Gen = new TRandom3(0);
	Gen->SetSeed();

int count=0;
int count1=0;
int N1=0;
int N2=0;
int N3=0;

int time_base=1000;//Длительность набора совпадений в секундах
int m=10000; //100 КГц = 10000 нс
int t0=230; //Интервал в котором ищем совпадение
int n=10000;//Количество задействованных ФЭУ

int *generator1;
int *generator2;
int *generator3;

for(int time=0; time<time_base; time++)
{
	printf("time: %d \n", time);

for (int i=0; i<n; i++)
	{
		N1=Gen->Poisson(1);
		//HistoPoisson1->Fill(N1);
		//printf("First number Poisson: %d\n", N1 );
		N2=Gen->Poisson(1);
		N3=Gen->Poisson(1);
		//HistoPoisson2->Fill(N2);
		//printf("Second number Poisson: %d\n", N2 );
		//printf("_____________________________________\n");
		generator1 = new int [N1];
		generator2 = new int [N2];
		generator3 = new int [N3];

		for (int j=0; j<N1; j++)
			{ 
				generator1[j]=Gen->Uniform(0,m);
				//printf("Gen_1:%d\n", generator1[j]);	
			}

		for (int j=0; j<N2; j++)
			{ 
				generator2[j]=Gen->Uniform(0,m);
				//printf("Gen_2:%d\n", generator2[j]);	
			}

		for (int j=0; j<N3; j++)
			{ 
				generator3[j]=Gen->Uniform(0,m);
				//printf("Gen_2:%d\n", generator2[j]);	
			}

		if ((N1>0) && (N2>0))
			{	
				for (int j1=0; j1<N1; j1++)
					{	
						for (int j2=0; j2<N2; j2++)
							{	
								if ((generator1[j1]-generator2[j2]>0) && (generator1[j1]-generator2[j2]<=t0))
									{	
										count++;
										count1++;
										//HistoGenerator->Fill(generator1[j1]);
									}
							}
					}
			}

		if ((N1>0) && (N3>0))
			{		
				for (int j1=0; j1<N1; j1++)
					{	
						for (int j3=0; j3<N3; j3++)
							{	
								if ((generator1[j1]-generator3[j3]>0) && (generator1[j1]-generator3[j3]<=t0))
									{	
										count++;
										count1++;
										//HistoGenerator->Fill(generator1[j1]);
									}
							}
					}	
			}
delete[] generator1;
delete[] generator2;
delete[] generator3;
	}


HistoMatches->Fill(count1);
//printf("%d\n", count1);
count1=0;
//printf("%d\n", time);

}
	
printf("***********************************************\n");
printf("General count matches: %d at time %d sec\n", count, time_base);
printf("From 1 sec: %f matches\n", float(count) / float(time_base));
printf("***********************************************\n");


gStyle->SetOptStat("eMR");
gStyle->SetStatFormat("4.5f");

TCanvas *Canvas = new TCanvas("Canvas","Task", 1400, 800);
//anvas->Divide(2,2);
//Canvas->cd(1);
//HistoPoisson1->Draw();
//Canvas->cd(2);
//HistoPoisson1->Draw();
//Canvas->cd(3);
HistoMatches->Draw();
//Canvas->cd(4);
//HistoGenerator->Draw();
}