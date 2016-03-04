class TowerHanoi
{
	public static void tower(int n, char fr, char tr, char ar)
	{
	    if (n == 1)
	    {
	        System.out.println("Move disk 1 from rod" + fr + " to rod " + tr);
	        return;
	    }
	    tower(n-1, fr, ar, tr);
	    System.out.println("Move disk" + n + "from rod" + fr +" to rod " + tr);
	    tower(n-1, ar, tr, fr);
	}
	public static void main(String[] args)
	{
		int number_of_disks = 4;
		tower(number_of_disks, 'A' , 'C' , 'B');
	}
}
