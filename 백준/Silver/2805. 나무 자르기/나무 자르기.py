import sys
def bs(s, e):
    global ans
    if s > e:
        return
    calc = 0
    m = (s+e)//2
    for h in highs:
        if h >= m:
            calc += h - m
    if calc < M:
        bs(s, m-1)
    else:
        ans = m
        bs(m+1, e)


input = sys.stdin.readline
N, M = map(int, input().split())
highs = list(map(int, input().split()))
highs.sort()
ans = 0
bs(1, highs[-1])
print(ans)