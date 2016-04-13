import java.io.*;
import java.util.Scanner;
class amit{
public class HelloWorld
{
	// int[][]	a;
	int count;
	public int dfg(int h)
	{
		System.out.println(h);
		int y,z,n;
		count+=1;
		System.out.println(count);
		if(count>10)
			return 1;
		y=0;z=1;
		n=fac(z);
		return 0;
	}
	public int fac(int h)
	{
		System.out.println(h);
		int y,z,n;
		count+=1;
		System.out.println(count);
		if(count>10)
			return 1;
		y=3;z=4;
		n =dfg(z);
		return 0;
	}
	public  void main() {
		int d,a,c,n,b;
        Scanner in ;
        in = new Scanner();
        count=0;
        // a= b;
        b=in.nextInt();
		c = dfg(b);//+fac(fac(b)/3)*fac(5);
		System.out.println(c);
	}
}
}