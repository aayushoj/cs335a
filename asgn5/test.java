// import java.io.*;
// class amit{
// public class HelloWorld
// {
// 	public static void main() {
// 	// g = A[1][2] + A[2][1];
// 		int a,b,c;
//     int[] A;
//     int g;
//     A = new int[4];
//     for(int i=0;i<4;i++)
//     {
//     	A[i]=i;
//     }
//     g = A[0];
//     System.out.println(g);
//     // int a;
// 	}
// }
// }

import java.io.*;
class amit{
public class HelloWorld
{
	int[][]	a;
	public static int fac(int h)
	{
		int y;
		
		a = new int[10][10];
		if(h==1)
			return 1;
		else
		{
			a[0][0]=a[5][6]=y=h*fac(h-1);
			int d  = a[5][6];
			System.out.println(d);
			return y;
		}
		
	}
	public static void main() {
		  int d,a,c,n,b;
        Scanner in;
        in = new Scanner();
        a= b;
        b=in.nextInt();
		  c = fac(b);
		  System.out.println(c);
	}
}
}