import java.text.DecimalFormat;
class ExactDecimalValue
{        
    final strictfp static public void main(String... arg)
    {    

      float f1=123.23.01;           
      float f2=124.0f;           
      float f3=f1+f2;

      System.out.println(f1+f2);
      System.out.println("sum of two floats:"+f3);

    }     
}