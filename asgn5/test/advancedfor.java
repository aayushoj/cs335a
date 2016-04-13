import java.io.*;
class amit{
public class HelloWorld
{
	public static void main() {
	// g = A[1][2] + A[2][1];
	int a,b;
    int[] A;
    int[] B;
    int[] c;
    int g;
    A = new int[40];
    B = new int[40];
    c= new int[50];
    int i;

    for(i=0;i<40;i++)
    {
    	if(i%2){
    		B[i]=i*2;
    		int j;
    		for(j=2;j<6;j++)
    		{
    			
    			if(j>3 && i%3)
    			{
    				break;
    			}
    			if(j%2)
    			{
    				System.out.println(-100000);
    				continue;
    			}
    			System.out.println(j);
    		}
    		A[i]=i;
    	}
    	else
    	{
    		B[i]=i*3;
    		if(i>10)
    		{
    			break;
    		}
    		A[i]=i;
    	}
    	System.out.println(i);
    }
    System.out.println(-1000);
    System.out.println(i);
    for(i=0;i<40;i++)
    {
    	c[i]=B[i]*A[i];
    	g=c[i];
    	System.out.println(g);
    }
    // g = A[0];
    // System.out.println(g);
	}
}
}

// import java.io.*;
// class amit{
// public class HelloWorld
// {
// 	int[][]	a;
// 	public static int fac(int h)
// 	{
// 		int y;
		
// 		a = new int[10][10];
// 		if(h==1)
// 			return 1;
// 		else
// 		{
// 			a[0][0]=a[5][6]=y=h*fac(h-1);
// 			int d  = a[5][6];
// 			System.out.println(d);
// 			return y;
// 		}
		
// 	}
// 	public static void main() {
// 		  int d,a,c,n,b;
//         Scanner in;
//         in = new Scanner();
//         a= b;
//         b=in.nextInt();
// 		  c = fac(b);
// 		  System.out.println(c);
// 	}
// }
// }