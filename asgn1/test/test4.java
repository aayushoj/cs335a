public static void bubblesort(int list[])
{
		int temp;
		int len= list.length;
		for(int i = 0; i < len; i++)
		{	
			for(int j = 0; j < len - i - 1; j++)
			{	
				if(list[j] > list[j+1])
				{	
					temp = list[j + 1];
					list[j + 1] = list[j];
					list[j] = temp;
				}
			}
		}
		// printing the sorted array 
		System.out.println("Sorted order of list is");
		
		for(int i= 0 ;i< len ;i++)
		{
			System.out.print(list[i] + " ");	
		}
}
