N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0] for _ in range(3)] for _ in range(N)]

for r in range(N):
    if r == 0:
        dp[r][0][0], dp[r][0][1] = board[0][0], board[0][0]
        dp[r][1][0], dp[r][1][1] = board[0][1], board[0][1]
        dp[r][2][0], dp[r][2][1] = board[0][2], board[0][2]
    else:
        dp[r][0][0] = max(dp[r-1][0][0], dp[r-1][1][0]) + board[r][0]
        dp[r][0][1] = min(dp[r-1][0][1], dp[r-1][1][1]) + board[r][0]
        dp[r][1][0] = max(dp[r-1][0][0], dp[r-1][1][0], dp[r-1][2][0]) + board[r][1]
        dp[r][1][1] = min(dp[r-1][0][1], dp[r-1][1][1], dp[r-1][2][1]) + board[r][1]
        dp[r][2][0] = max(dp[r-1][1][0], dp[r-1][2][0]) + board[r][2]
        dp[r][2][1] = min(dp[r-1][1][1], dp[r-1][2][1]) + board[r][2]

ans = [0, float('inf')]
for li in dp[-1]:
    ans[0] = max(ans[0], li[0])
    ans[1] = min(ans[1], li[1])

print(*ans)
