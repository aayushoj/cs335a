import java.io.*;
public class prime {
  
   public static void main() {
   		
   	   int primeslen = 50,prime2=20;
       Scanner in ;
       in = new Scanner();
       int num;
       num = in.nextInt();
       while(num<primeslen){
       	if(num/prime2)
       	{
       		System.out.printf("%d\n",-1);
       		if(num==35)
       		{
       			break;
       		}
       	}
       	else
       	{
       		if(num==5)
       		{
       			while(num<10)
       			{
       				num++;
       				System.out.printf("p1 %d\n",num);
       				if(num==9)
       				{
       					break;
       				}
       			}
       			continue;
       		}
       		System.out.printf("p2 %d\n",num);
       	}
       	num++;
       }
       // System.out.printf("%d\n",isPrime(num));
       // fillSieve();
   }
}
