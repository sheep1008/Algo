#include <stdio.h>
int main()
{
	char chess1 [8][8] = {
		'W','B','W','B','W','B','W','B',
		'B','W','B','W','B','W','B','W',
		'W','B','W','B','W','B','W','B',
		'B','W','B','W','B','W','B','W',
		'W','B','W','B','W','B','W','B',
		'B','W','B','W','B','W','B','W',
		'W','B','W','B','W','B','W','B',
		'B','W','B','W','B','W','B','W'
	};
	char chess2[8][8] = {
		'B','W','B','W','B','W','B','W',
		'W','B','W','B','W','B','W','B',
		'B','W','B','W','B','W','B','W',
		'W','B','W','B','W','B','W','B',
		'B','W','B','W','B','W','B','W',
		'W','B','W','B','W','B','W','B',
		'B','W','B','W','B','W','B','W',
		'W','B','W','B','W','B','W','B'
	};
	int n, m;
	int count_1;
	int count_2;
	int min = 100;
	scanf("%d %d", &n, &m);
	getchar();
	char bode[50][50];
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m+1; j++)
			scanf("%c", &bode[i][j]);
	}
	
	for (int i = 0; i < n - 7; i++)
	{
		for (int j = 0; j < m - 7; j++)
		{
			count_1 = 0;
			count_2 = 0;
			for (int c=0; c<8; c++)
			{
				for (int d = 0; d < 8; d++)
				{
					if (chess1[c][d] == bode[c + i][d + j])
						count_1++;
					if (chess2[c][d] == bode[c + i][d + j])
						count_2++;
					
				}
			}
			if (count_1 <= count_2 && count_1 < min)
				min = count_1;
			else if (count_1 > count_2 && count_2 < min)
				min = count_2;
		}
	}
	printf("%d", min);
}	