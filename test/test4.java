public static void bubblesort(int[] list)
	{
		assert list != null : "failed precondition";

		int temp;
		boolean changed = true;
		for(int i = 0; i < list.length && changed; i++)
		{	changed = false;
			for(int j = 0; j < list.length - i - 1; j++)
			{	assert (j > 0) && (j + 1 < list.length) : "loop counter j " + j +
					"is out of bounds.";
				if(list[j] > list[j+1])
				{	changed = true;
					temp = list[j + 1];
					list[j + 1] = list[j];
					list[j] = temp;
				}
			}
		}

		assert isAscending( list );
	}
