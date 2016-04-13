import java.io.*;
public class TowersOfHanoi {

   public void solve(int n, int start, int auxiliary, int end) {
       if (n == 1) {

           System.out.println(start);
           System.out.println(-1);
           System.out.println(end);
       } else {
           solve(n - 1, start, end, auxiliary);
           System.out.println(start);
           System.out.println(-1);
           System.out.println(end);
           solve(n - 1, auxiliary, start, end);
       }
   }

   public static void main() {
       // System.out.print("Enter number of discs: ");
       Scanner in ;
       in = new Scanner();
       int discs;
       discs = in.nextInt();
       solve(discs, 1, 2, 3);
   }
}