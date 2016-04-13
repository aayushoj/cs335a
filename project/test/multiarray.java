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
    	B[i]=i*2;
    	A[i]=i;
    	System.out.printf("%d\n",i);
    }
    for(i=0;i<40;i++)
    {
    	c[i]=B[i]*A[i];
    	g=c[i];
    	System.out.printf("%d\n",g);
    }
    // g = A[0];
    // System.out.printf("%d\n",g);
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
// 			System.out.printf("%d\n",d);
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
// 		  System.out.printf("%d\n",c);
// 	}
// }
// }