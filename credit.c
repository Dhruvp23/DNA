#include <cs50.h>
#include <stdio.h>
#include<string.h>

int main(void)
{
   int long CdNo = get_long("Enter Credit Card Number : ");
   
   int n = strlen(CdNo);
   //int n = 16;
   int st[n];

   for (int i=0;i<n;i=i+1)
   {
       st[i] = CdNo % 10;
       CdNo = CdNo / 10;
   }

for (int j=1;j<n;j=j+2)
 {
     st[j]=st[j] * 2;
     printf("%d ",st[j]);

 }

 printf("\n");
 int sum =0 ;

for (int k=1;k<n;k=k+2)
 {
    if(st[k] > 9)
    {
       int mod = st[k] % 10;
      st[k] = 1 + mod;
    }
    else
    {
        st[k] = st[k];
    }

printf("%d ",st[k]);
   sum = sum + st[k];
 }

 printf("\n");
 printf("%d \n",sum);

 int add = 0;
   for (int d=0;d<n;d=d+2)
   {
       add = add + st[d];

     printf("%d ",st[d]);
   }

   printf("\n");
   add = add + sum;
  printf("%d \n",add);

if (add % 10 == 0)
   {
       printf("valid");
    }
    else
    {
       printf("invalid");
   }
   printf("\n");
}
