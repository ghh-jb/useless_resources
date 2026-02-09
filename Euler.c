#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

long long euler(long long n) {
    long long res = n;
    long long x = n;
    
    for (long long p = 2; p * p <= x; p++) {
        if (x % p == 0) {
            while (x % p == 0) {
                x /= p;
            }
            res -= res / p;
        }
    }
    
    if (x > 1) {
        res -= res / x;
    }
    
    return res;
}
