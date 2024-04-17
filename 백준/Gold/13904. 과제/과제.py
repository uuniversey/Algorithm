import heapq, sys

input = sys.stdin.readline
N = int(input())
hq = []
memo = 0

for _ in range(N):
    D, W = list(map(int, input().split()))
    heapq.heappush(hq, (-W, D))
    memo = max(memo, D)

check = [0] * (memo+1)
ans = 0
while hq:
    point, day = heapq.heappop(hq)
    point = -point

    for i in range(day, 0, -1):
        if not check[i]:
            check[i] = 1
            ans += point
            break
        else:
            pass

print(ans)