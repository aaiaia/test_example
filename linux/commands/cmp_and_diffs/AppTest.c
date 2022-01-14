#include<stdio.h>
#include<SharedTest_0.h>
#include<SharedTest_1.h>
 
int main(int argc, char** argv)
{
    for(unsigned int i = 0; i < argc; i++)
    {
        printf("arg[%d] %s\r\n", i, argv[i]);
    }
 
    printf("4 + 2 = %d\r\n", add_0(4,2));
    printf("4 - 2 = %d\r\n", sub_0(4,2));
    printf("4 * 2 = %d\r\n", mul_0(4,2));
    printf("4 / 2 = %d\r\n", div_0(4,2));
 
    printf("4 + 2 = %d\r\n", add_1(4,2));
    printf("4 - 2 = %d\r\n", sub_1(4,2));
    printf("4 * 2 = %d\r\n", mul_1(4,2));
    printf("4 / 2 = %d\r\n", div_1(4,2));
 
    return 0;
}
