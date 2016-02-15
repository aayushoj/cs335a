#include<stdio.h>
#include<math.h>

int main()
{
  double n;
  int exp[]={0,0,0,0,0,0,0,0},mant[23];
  int sign=0;
  int j;
  for(j=0;j<23;j++)
     mant[j]=0;
  
  scanf("%lf", &n);
  if(n<0)
  {
     sign =1;
     n=-n;
  }
  
  double t=n;
  int expn=0;
  if(t>1)
  {
    while(t>2)
    {
       t=t/2;
       expn++;
    }
  }
  else
  {  
    while(t<1)
    {
       t=t*2;
       expn--;
    } 
  }
  
  expn=expn+127;
  j=0;
  while(expn!=0)
  {
    exp[7-j]=expn%2;
    expn=expn/2;
    j++;
  }
  
  double mnts=t-1;
  j=0;
  while(mnts!=1 && j<23)
  {
    mnts=mnts*2;
    if(mnts>=1)
    {
       mant[j]=1;
       mnts=mnts-1;
    }
    j++;
  }
   
  printf("The number %lf is converted to %d  ",n, sign);
  int i;
  for(i=0;i<8;i++)
  {
     printf("%d", exp[i]);  
  }
  printf("  ");
  for(i=0;i<23;i++)
  {
     printf("%d", mant[i]);
  }  
  printf("\n");
  
  int expconv=0;
  double mantconv=0.0,conv;
  for(i=7;i>=0;i--)
  {
    expconv=expconv+exp[7-i]*pow(2,i);
  }
  int pwr;
  for(i=0;i<23;i++)
  {
    pwr=-i-1;
    mantconv=mantconv+mant[i]*pow(2,pwr);
  }
  conv=pow(-1,sign)*(1+mantconv)*pow(2,expconv-127);
  printf("When converted back, it becomes %lf\n",conv);  
}
