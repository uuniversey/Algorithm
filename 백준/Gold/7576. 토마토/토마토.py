from collections import deque

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
tom, wall = deque([]), deque([])
vt = [[0] * N for _ in range(M)]
for r in range(M):
    for c in range(N):
        if box[r][c] == 1:
            tom.append((r, c))
        elif box[r][c] == -1:
            wall.append((r, c))

for t in tom:
    vt[t[0]][t[1]] = 1

for w in wall:
    vt[w[0]][w[1]] = 1

while tom:
    x, y = tom.popleft()
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N and box[nx][ny] != -1:
            if vt[nx][ny] == 0:
                vt[nx][ny] = vt[x][y] + 1
                tom.append((nx, ny))

            elif vt[nx][ny] != 0:
                if vt[nx][ny] > vt[x][y] + 1:
                    vt[nx][ny] = vt[x][y] + 1
                    tom.append((nx, ny))

res = 0
error = 0
for r1 in range(M):
    for c1 in range(N):
        res = max(vt[r1][c1], res)
        if not vt[r1][c1]:
            error = 1

if not error:
    print(res-1)
else:
    print(-1)