#include <stdio.h>

int main () {
    int A, B, C;
    scanf("%d %d", &A, &B);
    scanf("%d", &C);
    
    int calc;
    calc = A*60+B+C;
    
    if (calc >= 1440) {
        calc -= 1440;
    }
    printf("%d %d", calc / 60, calc % 60);
    
    return 0;
}