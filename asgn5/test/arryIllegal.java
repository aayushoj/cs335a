import java.io.*;
class amit{
public class HelloWorld
{
	public static void main() {
	// g = A[1][2] + A[2][1];
	int a,b,c;
    int[] A;
    int[] B;
    int g;
    A = new int[4];
    B = new int[2];
    int i;
    for(i=0;i<4;i++)
    {
    	B[i]=i;
    	A[i]=i;
    	System.out.println(i);
    }
    for(i=0;i<4;i++)
    {
    	g=A[i];
    	System.out.println(g);
    }
    g = A[0];
    System.out.println(g);
	}
}
}