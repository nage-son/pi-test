#include <stdio.h>

int main() {
    int n = 5;

    int result = n << 3;

    printf("result >>> %d\n", result);

    int a = 100;

    a &= 3;

    printf("a >>> %d\n", a);

    return 0;
}