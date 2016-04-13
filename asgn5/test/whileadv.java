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
       		System.out.printf("-1");
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
       				System.out.printf("Inside the second loop/n");
       				System.out.printf("%d",num);
       				if(num==9)
       				{
       					break;
       				}
       			}
       			continue;
       		}
       		System.out.printf("%d",num);
       	}
       	num++;
       }
       // System.out.println(isPrime(num));
       // fillSieve();
   }
}