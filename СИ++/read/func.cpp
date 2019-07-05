
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
	for(i=0;i<23;i++)
	{
		int j=22-i;
		int step=((number>>j) & 1);
		fraction = fraction + step*pow(2,(-1-f));
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
