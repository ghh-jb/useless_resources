#include <stdio.h>
// actually now wop, but pow
// anyway
double fasp_wop(double a, int n) {
    double r = 1.0;
    int flag = 0;
    
    if (n < 0) {
        flag = 1;
        n = -n;
    }
    
    while (n) {
        if (n & 1) {
            r *= a;
        }
        a *= a;
        n >>= 1;
    }
    
    if (flag) {
        r = 1.0 / r;
    }
    
    return r;
}
