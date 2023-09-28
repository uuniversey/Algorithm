def plus(d, h, memo):
    calc = 0
    if d == 0:
        return h

    if memo[d][h] != 0:
        return memo[d][h]

    for i in range(h):
        calc += plus(d-1, h-i, memo)

    memo[d][h] = calc
    return calc

T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    memo = [[0] * (n+1) for _ in range(k+1)]
    print(plus(k, n, memo))