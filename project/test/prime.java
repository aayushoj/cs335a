import java.io.*;
public class prime {
	
	int[] primes;

	int primeslen;

	public int isPrime(int n) {
	    for(int i=2;i<n;i++) {
	        if(n%i==0)
	            return 0;
	    }
	    return 1;
	}
	public void fillSieve() {
		int g;
		System.out.printf("%d\n",primeslen);
	    for (int i=2;i<primeslen;i++) {
	    	primes[i]=1;
	    }
	    for (int i=2;i<primeslen;i++) {
	        if(primes[i]) {
	            for (int j=2;i*j<primeslen;j++) {
	                primes[i*j]=0;
	            }
	        }
	    }
	    for (int i=2;i<primeslen;i++) {
	    	g=primes[i];
	    	if(g ==1)
	    	{
	    	System.out.printf("%d is a prime\n",i);
	    	}
	    }
	}

  
   public static void main() {
   		primes = new int[50];
   		primeslen = 50;
       Scanner in ;
       in = new Scanner();
       int num;
      // num = in.nextInt();
        //System.out.printf("%d\n",isPrime(num));
       fillSieve();
   }
}
