N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(1, N):
        if j + 1 < N and home[i][j + 1] == 0:
            dp[i][j + 1][0] = dp[i][j][0] + dp[i][j][2]

        if i + 1 < N and home[i + 1][j] == 0:
            dp[i + 1][j][1] = dp[i][j][1] + dp[i][j][2]

        if i + 1 < N and j + 1 < N and home[i + 1][j] == 0 and home[i][j + 1] == 0 and home[i + 1][j + 1] == 0:
            dp[i + 1][j + 1][2] = dp[i][j][0] + dp[i][j][1] + dp[i][j][2]

answer = sum(dp[N - 1][N - 1])
print(answer)