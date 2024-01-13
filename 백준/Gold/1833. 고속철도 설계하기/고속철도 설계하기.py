def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    parent[max(x, y)] = min(x, y)


N = int(input())
adj_l = [list(map(int, input().split())) for _ in range(N)]
C = 0
M = 0
parent = [_ for _ in range(N+1)]
link_info = []
cost_info = []
n = 0
for li in adj_l:
    n += 1
    for m in range(n-1, N):
        if li[m] < 0:
            link_info.append([-li[m], n, m+1])
        else:
            if li[m] != 0:
                cost_info.append([li[m], n, m+1])

for c, x, y in link_info:
    union(x, y)
    C += c

cost_info.sort()
record = []
for c, x, y in cost_info:
    if find(x) != find(y):
        union(x, y)
        C += c
        M += 1
        record.append([x, y])

print(C, M)
for a, b in record:
    print(a, b)