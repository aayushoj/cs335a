import java.io.*;
class looping{
	public static void main(String[] args) {
        int i;
        i=5;
		 for(i=2;i<5;i++)
		 {
		 	System.out.println(i);
		 }
		 for(i=2;i<5;)
		 {
		 	System.out.println(i);
		 	i++;
		 }
		 for(;i<5;i++)
		 {
		 	System.out.println(i);
		 }
		 for(;;)
		 {
		 	if(i==5)
		 	{
		 		break;
		 	}
		 	System.out.println(i);
		 }
		 
	}
}

