N, M = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_l[a].append(b)
    adj_l[b].append(a)

res = [50000]
for i in range(1, N+1):
    vt = [0] * (N+1)
    q = [i]
    vt[i] = 1
    while q:
        p = q.pop(0)
        for j in adj_l[p]:
            if not vt[j]:
                q.append(j)
                vt[j] = vt[p] + 1

    res.append(sum(vt))

print(res.index(min(res)))