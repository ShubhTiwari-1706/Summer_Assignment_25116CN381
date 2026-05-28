#include <stdio.h>

int main(){
    int num,sum=0,i;
    printf("enter number");
    scanf("%d",&num);
    for (i=1;i<=num;i++){
        sum = sum+i;
    }
    printf("%d",sum);
    return 0;
}