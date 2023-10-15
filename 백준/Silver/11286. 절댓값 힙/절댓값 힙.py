import heapq, sys

N = int(input())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heapq.heappush(hq, (abs(x), x))
    else:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])