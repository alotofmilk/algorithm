#include<stdio.h>
int n,c;
int main(){
scanf("%d",&n);
for(int i=1; i<=n;i++) if(i<100||i%10+i/100==i/10%10*2)c++;
printf("%d",c);
}