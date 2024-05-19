#include <stdio.h>

int main(void)
{
	int submit[30];
	int s;
	int i,a;
	for (i = 0; i < 30; i++)
	{
		submit[i] = i + 1;
	}
	

	for (i = 0; i < 28; i++)
	{
		scanf("%d", &s);
		for (a = 0; a < 30; a++)
		{
			if (submit[a] == s)
			{
				submit[a] = 0;
			}
		}
	}
	for (i = 0; i < 30; i++)
	{
		if (submit[i] != 0)
		{
			printf("%d\n", submit[i]);
		}
	}

	return 0;
}