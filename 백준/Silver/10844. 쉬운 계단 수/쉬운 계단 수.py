n = int(input())
dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
while n >= 2:
    c_dp = [0] * 10
    for i in range(10):
        if i == 0:
            c_dp[i] = dp[i+1]
        elif i == 9:
            c_dp[i] = dp[i-1]
        else:
            c_dp[i] = dp[i-1] + dp[i+1] 

    dp = c_dp
    n -= 1

print(sum(dp) % 1000000000)

