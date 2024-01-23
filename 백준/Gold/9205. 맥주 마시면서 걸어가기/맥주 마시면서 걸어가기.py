import sys

def dfs(s):
    global ans
    if s == n+1:
        ans = 'happy'
        return

    vstd[s] = 1
    mx, my = market[s]
    for idx, val in enumerate(market):
        x, y = val
        if vstd[idx] == 0 and abs(x - mx) + abs(y - my) <= 1000:
            vstd[idx] = 1
            dfs(idx)


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    market = (
                [list(map(int, input().split()))] +
                [list(map(int, input().split())) for _ in range(n)] +
                [list(map(int, input().split()))]
              )

    vstd = [0] * (n+2)
    ans = 'sad'
    dfs(0)
    print(ans)