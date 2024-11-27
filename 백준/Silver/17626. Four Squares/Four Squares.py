n = int(input())
dp = [5] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    j = 1
    while j**2 <= i:
        dp[i] = min(dp[i], dp[i-j**2] + 1)
        j += 1

print(dp[n])