import java.io.*;
class amit{
public class HelloWorld
{
    // int[][] a;
    public int rec(int n)
    {
    	System.out.printf("%d\n",n);
       if(n<12){
        return n;
       }
       else
       {
         int a,b,c;
         a= rec(n/2) + rec(n/3) + rec(n/4);
         //System.out.println(a);
         if(a<n)
         {
            return n;
         }
         else
         {
            return a;
         }
       }
    }
    public static void main() {
        Scanner in;
        in = new Scanner();
          int x,y;
          int n =1000;
          y = in.nextInt();
          int ans = rec(y);
          System.out.println(ans);
        }
}
}

