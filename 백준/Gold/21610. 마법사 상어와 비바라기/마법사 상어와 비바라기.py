from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
delta = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
# 대각 2, 4, 6, 8
cloud = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])


for i in range(M):
    d, s = map(int, input().split())
    C = len(cloud)
    vstd = [[0] * N for _ in range(N)]

    for j in range(C):
        di, dj = delta[d]
        cloud[j][0] += di * s
        cloud[j][1] += dj * s

        for k in range(2):
            if cloud[j][k] >= N:
                cloud[j][k] -= (cloud[j][k] // N) * N
            elif cloud[j][k] < 0:
                if cloud[j][k] % N == 0:
                    cloud[j][k] += (-cloud[j][k] // N) * N
                else:
                    cloud[j][k] += ((-cloud[j][k] // N) + 1) * N

        grid[cloud[j][0]][cloud[j][1]] += 1
        vstd[cloud[j][0]][cloud[j][1]] = 1

    for m in range(C):
        bug = 0
        for l in range(4):
            ni, nj = delta[2*l+2]
            if 0 <= cloud[m][0] + ni < N and 0 <= cloud[m][1] + nj < N:
                if grid[cloud[m][0] + ni][cloud[m][1] + nj] != 0:
                    bug += 1

        grid[cloud[m][0]][cloud[m][1]] += bug

    for row in range(N):
        for col in range(N):
            if grid[row][col] >= 2 and vstd[row][col] == 0:
                grid[row][col] -= 2
                cloud.append([row, col])

    for _ in range(C):
        cloud.popleft()

res = 0
for r in range(N):
    for c in range(N):
        res += grid[r][c]

print(res)