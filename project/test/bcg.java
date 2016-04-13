import java.io.*;
class amit{
public class HelloWorld
{
	int[][]	a;
	public static void main() {
        Scanner in;
        in = new Scanner();
          int[] A;
          A = new int[1000];
          for(int i=1;i<1000;i++)
          {
          int p,q;
          p=q;
           int z = 0;
              if(i<12)
              {
                  A[i]=i;
              }
              else
              {
                  int x = A[i/2]+A[i/3]+A[i/4];
                  if(x < i)
                  {
                    A[i] = i;
                  }
                  else
                  {
                    A[i] = x;
                  }
              }
             z = A[i];
		    System.out.printf("%d\n",z);
          }
	}
}
}
