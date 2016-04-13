import java.io.*;
class amit{
public class HelloWorld
{
	 int count;
	public static int fac(int h)
	{
		int y;
		 if(h==1)
		 	return 1;
		 else
		 {
		 	// a[0][0]=a[5][6]=y=h*fac(h-1);
		 	// int d  = a[5][6];
		 	y=fac(h-1);
		 	System.out.printf("%d\n",y*h);
		 	return y*h;
		 }
		
	}
	public static void main() {
		int d,a,c,n,b;
        Scanner in;
        in = new Scanner();
        count=0
        // a= b;
        b=in.nextInt();
		c = fac(b)+fac(fac(b)/3)*fac(5);
		System.out.printf("%d\n",c);
	}
}
}
