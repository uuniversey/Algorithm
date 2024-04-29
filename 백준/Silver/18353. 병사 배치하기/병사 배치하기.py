import sys
input = sys.stdin.readline
N = int(input())
power = list(map(int, input().split()))
dp = [1] * N
memo = 10000000

for i in range(1, N):
    for j in range(0, i):
        if power[i] < power[j]:
            dp[i] = max(dp[i], dp[j] + 1)

res = max(dp)
print(N-res)