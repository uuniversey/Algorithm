import heapq,sys

N = int(input())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if not x:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))

    else:
        heapq.heappush(hq, x)