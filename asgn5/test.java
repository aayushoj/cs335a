import java.io.*;
class amit{
public class HelloWorld
{
	int b,n;
	public static void fac()
	{
		if(n==1)
		{
			return;
		}
		else
		{
			b = b* n;
			n = n - 1;
		}
		
	}
	public static void main() {
        Scanner in;
        in = new Scanner();
        b = 1;
        n=in.nextInt();
		  fac();
	}
}
}
