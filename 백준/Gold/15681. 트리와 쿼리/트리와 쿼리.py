import sys
sys.setrecursionlimit(10**9)

def countquery(x):
    dp[x] = 1
    for t in Tree[x]:
        if dp[t] == 0:
            countquery(t)
            dp[x] += dp[t]


input = sys.stdin.readline

N, R, Q = map(int, input().split())
Tree = [[] for _ in range(N+1)]
dp = [0] * (N+1)
for _ in range(N-1):
    U, V = map(int, input().split())
    Tree[U].append(V)
    Tree[V].append(U)

countquery(R)

for _ in range(Q):
    node = int(input())
    print(dp[node])
