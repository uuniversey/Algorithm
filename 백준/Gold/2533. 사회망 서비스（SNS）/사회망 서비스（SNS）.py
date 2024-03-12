import sys
sys.setrecursionlimit(10**8)


def EA(s):
    dp[s][1] = 1
    for i in sns[s]:
        if vstd[i] == 0:
            vstd[i] = 1
            EA(i)

            dp[s][0] += dp[i][1]
            dp[s][1] += min(dp[i][0], dp[i][1])


input = sys.stdin.readline
N = int(input())
sns = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    sns[u].append(v)
    sns[v].append(u)
vstd = [0] * (N+1)
vstd[1] = 1
dp = [[0, 0] for _ in range(N+1)]
EA(1)

print(min(dp[1]))
