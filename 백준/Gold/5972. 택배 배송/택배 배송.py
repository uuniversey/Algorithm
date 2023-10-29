import heapq

N, M = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
vt = [float('inf')] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    adj_l[A].append((C, B))
    adj_l[B].append((C, A))

vt[1] = 0
hq = [(0, 1)]
while hq:
    val, position = heapq.heappop(hq)
    for v, p in adj_l[position]:
        if vt[p] > vt[position] + v:
            vt[p] = vt[position] + v
            heapq.heappush(hq, (vt[p], p))

print(vt[N])