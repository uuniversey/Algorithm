from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
cand = []
vir = []
res = 0
for r in range(N):
    for c in range(M):
        if area[r][c] == 2:
            vir.append((r, c))
        elif area[r][c] == 0:
            cand.append((r, c))

memo = deepcopy(area)
combs = combinations([i for i in range(len(cand))], 3)
for co in combs:
    for k in range(3):
        x, y = cand[co[k]]
        area[x][y] = 1

    vt = [[0] * M for _ in range(N)]
    q = deepcopy(vir)
    while q:
        p = q.pop()
        area[p[0]][p[1]] = 2
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = di+p[0], dj+p[1]
            if 0 <= ni < N and 0 <= nj < M and vt[ni][nj] == 0 and area[ni][nj] == 0:
                q.append((ni, nj))
                vt[ni][nj] = 1

    num = 0
    for r1 in range(N):
        for c1 in range(M):
            if area[r1][c1] == 0:
                num += 1

    res = max(res, num)
    area = deepcopy(memo)

print(res)