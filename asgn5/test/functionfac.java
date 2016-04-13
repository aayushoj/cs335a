import java.io.*;
class amit{
public class HelloWorld
{
	// int[][]	a;
	// int count;
	public static int fac(int h)
	{
		int y,z;
		for (z=0;z<10;z++)
		{
			if(z>5)
			{
				System.out.println(-12);
				break;
				System.out.println(-323);
				continue;
			}
			else
			{
				System.out.println(z);
			}

		}
		// a = new int[10][10];
		// if(h==1)
		// 	return 1;
		// else
		// {
		// 	// a[0][0]=a[5][6]=y=h*fac(h-1);
		// 	// int d  = a[5][6];
		// 	y=fac(h-1);
		// 	System.out.println(y*h);
		// 	return y*h;
		// }
		
	}
	public static void main() {
		int d,a,c,n,b;
        Scanner in;
        in = new Scanner();
        count=0
        // a= b;
        b=in.nextInt();
		c = fac(b);//+fac(fac(b)/3)*fac(5);
		System.out.println(c);
	}
}
}