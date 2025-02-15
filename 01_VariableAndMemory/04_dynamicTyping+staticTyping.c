//This program is an example of Static Programming

#include<stdio.h>

int main(){
    int number = 25;
    float fraction = 2.5;
    char character = 'a';
    char sayHello[] = {'H','e','l','l','o','\0'};

    printf("Here the integer variable is %d\n", number);
    printf("Here the fraction variable is %f\n", fraction);
    printf("Here the character variable is %c\n", character);
    printf("If you happy than say %s\n", sayHello);

    printf("As you can see, we need to specify the variable type along with the variable name.\n");
    printf("This is why it is called static typing as we can see, the memory or variable names are ,\n");
    printf("Not handled by the memory manager and that's why no dynamic changes are happening.\n");
}
