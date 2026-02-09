#include <stdio.h>
// whatever, it is just c
int count_divisors(int x) {
    int cnt = 0;
    for (int i = 1; i * i <= x; i++) {
        if (x % i == 0) {
            if (i * i == x) {
                cnt++;
            } else {
                cnt += 2;
            }
        }
    }
    return cnt;
}
