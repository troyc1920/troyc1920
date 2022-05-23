#include <stdio.h>

int main(void){
    double a, b, c, min, mid, max;
    printf("Please input three numbers: ");
    scanf("%lf %lf %lf",&a,&b,&c);
    
    if (a > b){
        mid = a;
        min = b;
    } else{
        mid = b;
        min = a;
    }
    if (mid > c){
        max = mid;
        if (min > c){
            mid = min;
            min = c;
        } else{
            mid = c;
        }
    } 
    else {
        max = c;
    }
    
    printf("Sorting smallest to largest: %lf %lf %lf",min, mid, max);
    return 0;






}