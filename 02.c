#include <stdio.h>
#define MAX_SIZE 10

int hex2int(char val[]){
    int i = 0;
    int len = 0, b = 1,deci = 0;
    for(i;val[i]!='\0';i++){
        len++;
    }
    i=len-1;
    for(i; i>=0; i--){
        if(val[i]>='0' && val[i]<='9')          
            deci += (val[i] - 48)*b;
        else if(val[i]>='A' && val[i]<='F')
            deci += (val[i] - 55)*b;
            b = b * 16;
    }
    return deci;

}

int main(void){

    char str[MAX_SIZE],s1[MAX_SIZE],s2[MAX_SIZE], op;
    int a=0,b=0,count=0;
    double res;

    printf("Please input a hex formula: "); 
    scanf("%s",str);
    int i = 0;
    for(i;str[i]!='\0';i++){
        if(!(str[i]=='+' ||str[i]=='-' ||str[i]=='*' ||str[i]=='/')){
            s1[a]=str[i];
            a++;
            }
        else{
            op=str[i];
            count=i;
            break;
            }   
    }
    s1[a]='\0';
    i = count;
    for(i;str[i]!='\0';i++){
        if(!(str[i]=='+' ||str[i]=='-' ||str[i]=='*' ||str[i]=='/')){
            s2[b]=str[i];
            b++;
            }
    }

    s2[b]='\0';
    printf("two hex numbers are %s and %s",s1,s2);
    int n1=hex2int(s1);
    int n2=hex2int(s2);
    printf("\ncorresponding integers are %d and %d",n1,n2);

    switch(op){

        case '+':printf("\nresult in decimal: %d",n1+n2);
            break;

        case '-':printf("\nresult in decimal: %d",n1-n2);
            break;

        case '*':res=(double)n1*n2;
            printf("\nresult in decimal: %.4e",res);
            break;

        case '/':res=(double)n1/n2;
            printf("\nresult in decimal: %.4e",res);
            break;

    }

    return 0;
}