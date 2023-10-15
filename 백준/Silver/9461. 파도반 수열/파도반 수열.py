T = int(input())
for _ in range(T):
    N = int(input())
    memo = [0] * 101
    memo[1], memo[2], memo[3], memo[4], memo[5] = 1, 1, 1, 2, 2
    for n in range(6, 101):
        memo[n] = memo[n-1] + memo[n-5]

    print(memo[N])