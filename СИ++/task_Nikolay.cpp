void task_Nikolay()
{
TH1D *HistoPoisson = new TH1D ("HistoMatches", "Count_zero", 100, 0, 12);

TRandom3 *Gen = new TRandom3(0);
	Gen->SetSeed();

int time_base=10000;
int time_step = 1000;
int count_zero = 0;
int *generator;
int total_zero = 0;

for(int time=0; time<time_base; time++)
{
	generator = new int [time_step];
	total_zero = total_zero + count_zero;
	count_zero = 0;

	for (int i=0; i<time_step; i++)
	{
		generator[i] = Gen->Poisson(5.83);

		if (generator[i] == 0)
		{
			count_zero = count_zero + 1;
		}
	}
	HistoPoisson->Fill(count_zero);
	delete[] generator;
}
//printf("Number of zero: %d\n", total_zero);
TCanvas *Canvas = new TCanvas("Canvas","Task", 1400, 800);
HistoPoisson->Draw();

}


		
		
