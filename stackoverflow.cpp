#include <stdio.h>
int overflow(int a) {
    return overflow(123);
}
int main() {
    printf("Hello!");
    overflow(123);
    return 0;
}