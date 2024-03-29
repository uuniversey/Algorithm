import heapq, sys
input = sys.stdin.readline

N = int(input())
M = int(input())
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    adj_l[s].append((cost, e))

start, end = map(int, input().split())

vstd = [float('inf')] * (N+1)
hq = [(0, start)]
vstd[start] = 0
while hq:
    val, idx = heapq.heappop(hq)
    if val >= vstd[end]:
        continue

    for v, i in adj_l[idx]:
        if vstd[i] > val+v:
            heapq.heappush(hq, (val+v, i))
            vstd[i] = val+v

print(vstd[end])