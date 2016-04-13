import java.io.*;
class amit{
public class HelloWorld
{
	int[][]	a;
	//public static int fac(int h)
	//{
		//int y;

		//a = new int[10][10];
		//if(h==1)
			//return 1;
		//else
		//{
			//a[0][0]=a[5][6]=y=h*fac(h-1);
			//int d  = a[5][6];
			//System.out.println(d);
			//return y;
		//}

	//}
	public static void main() {
		  //int d,a,c,n,b;
        Scanner in;
        in = new Scanner();
          int[][] A;
          A = new int[3][3];
          int[][] B;
          B = new int[3][3];
          int[][] C;
          C = new int[3][3];
          int n=3;
          int c=0;
          for(int i=0;i<n;i++)
          {
          	for(int j=0;j<n;j++)
          	{
          		c++;
          		A[i][j]=c;
          	}
          }
          int d=1;
          for(int i=0;i<n;i++)
          {
          	for(int j=0;j<n;j++)
          	{
          		d++;
          		B[i][j]=d;
          		C[i][j]=0;
          	}
          }
          for(int i=0;i<n;i++)
          {
          	for(int j=0;j<n;j++)
          	{
          		for(int k=0;k<n;k++)
          		{
          			C[i][j]= C[i][j] + A[i][k]*B[k][j];
          		}
          	}
          }
          int ans=0;
          int yu;
          for(int i=0;i<n;i++)
          {
          	for(int j=0;j<n;j++)
          	{
          		yu = C[i][j];
          		System.out.printf("%d ",yu);
          		ans += C[i][j];
          	}
          	System.out.printf("\n");
          }
          System.out.println(ans);
	}
}
}
