#include <stdio.h>

int main(){
    int count = 0,i,num;
    printf("enter number:");
    scanf("%d",&num);
    while (num>0){
        num = num / 10;
        count++;
    }
    printf("the number of digits in the entered number is %d",count);
    return 0;
}