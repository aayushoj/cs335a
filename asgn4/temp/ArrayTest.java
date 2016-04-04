
import java.io.*;
public class HelloWorld
{
    int i;
	public static void main(String[] args) {
		int[] A;
        A=new int[100];
        int n=5,m=9;
        for(int i=0;i<n;i++)
        {
            A[i]=i;
        }
        for(int i=0;i<n;i++)
        {
            A[i*i+A[i]] = A[i+i];
        }
        for(int i=0;i<n*n;i++)
        {
            for(int j=0;j<m;)
            {
                A[i] =A[j]+A[j];
                j++;   
            }
        }
        //Ultimate For loop and Array test
        for(i=0;i<n*n;i++)
        {
            A[i*i+A[i]] = A[i+i]=A[n]+=A[i*i-i/i];
            A[i*i+A[i]] = A[i+i]=A[n]+=A[i*i-i%7];
        }
	}
}

