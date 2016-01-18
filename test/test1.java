// asdas
/*  The HelloWorldApp class implements an application that
  simply prints "Hello World!" to standard output.
 */
class HelloWorldApp {
    public static void main(String[] args) {
        int system=2;
        System.out.println("Hello World!"); // Display the string.
    }
}
class MyClass {
   int he12ight;
   int height2;
   MyClass() {
      System.out.println("bricks");
      height = 0;
   }
   MyClass(int i) {
      System.out.println("Building new House that is "
      + i + " feet tall");
      height = i;
      public class MainClass {
         public static void main(String[] args) {
            int nDisks = 3;
            doTowers(nDisks, 'A', 'B', 'C');
         }
         public static void doTowers(int topN, char from,
         char inter, char to) {
            if (topN == 1){
               System.out.println("Disk 1 from "
               + from + " to " + to);
            }else {
               doTowers(topN - 1, from, to, inter);
               System.out.println("Disk "
               + topN + " from " + from + " to " + to);
               doTowers(topN - 1, inter, from, to);
            }
         }/*  The HelloWorldApp class implements an application that
           simply prints "Hello World!" to standard output.
          */
      }//*/
   }
   void info() {
      System.out.println("House is " + height
      + " feet tall");
   }
   void info(String s) {
      System.out.println(s + ": House is "
      + height + " feet tall");
   }
}
