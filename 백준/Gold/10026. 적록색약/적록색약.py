import copy

def bfs():
    while q:
        r, c = q.pop()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N:
                if not vt[nr][nc] and color == area[nr][nc]:
                    q.append([nr, nc])
                    vt[nr][nc] = num


def bfs2():
    while q2:
        r, c = q2.pop()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N:
                if not vt2[nr][nc] and color2 == area2[nr][nc]:
                    q2.append([nr, nc])
                    vt2[nr][nc] = num2


N = int(input())
area = [list(input()) for _ in range(N)]
area2 = copy.deepcopy(area)
for k in range(N):
    for l in range(N):
        if area2[k][l] == 'G':
            area2[k][l] = 'R'
vt = [[0] * N for _ in range(N)]
vt2 = [[0] * N for _ in range(N)]
num = 1
num2 = 1
q = [[0, 0]]
q2 = [[0, 0]]
vt[0][0] = 1
vt2[0][0] = 1
color = area[0][0]
color2 = area2[0][0]
bfs()
bfs2()

for i in range(N):
    for j in range(N):
        if not vt[i][j]:
            num += 1
            q.append([i, j])
            color = area[i][j]
            bfs()

        if not vt2[i][j]:
            num2 += 1
            q2.append([i, j])
            color2 = area2[i][j]
            bfs2()

print(num, num2)