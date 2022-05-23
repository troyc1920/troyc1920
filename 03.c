# include <stdio.h>

int main(){
    printf("Please type in the characters: ");
    char c[100];
    scanf("%s",c);
    int len = 0;

    while (c[len] != '\0'){
        len ++;
    }
    char rev[len];
    for (int i=0;i<len;i++){
        /* checks to see if character is lower case 
        and converts it to upper case */
        if (c[i] > 64 && c[i] < 91){
            c[i] = c[i] + 32;
        }
        /* checks to see if character is upper case 
        and converts it to lower case */
        else if (c[i] > 96 && c[i] < 123){
            c[i] = c[i] - 32;
        }
    }
    printf("\nConvert little letter to big and big letter to little: %s \n", c);
    int i, j;
    j = len - 1;
    for (i=0;i<len;i++){
        rev[i] = c[j--];
    }
    rev[i] = '\0';
    printf("Reverse the converted characters: %s", rev);
    return 0;
}