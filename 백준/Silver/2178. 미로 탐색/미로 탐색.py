N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
vstd = [[0] * M for _ in range(N)]

vstd[0][0] = 1
q = [(0, 0, 1)]
while q:
    r, c, n = q.pop(0)
    if r == N-1 and c == M-1:
        print(n)
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] and not vstd[nr][nc]:
            vstd[nr][nc] = 1
            q.append((nr, nc, n+1))

