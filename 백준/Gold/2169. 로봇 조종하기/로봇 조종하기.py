N, M = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

for j in range(1, M):
    ground[0][j] += ground[0][j-1]

for r in range(1, N):
    left = [ground[r][c] + ground[r-1][c] for c in range(M)]
    right = [ground[r][c] + ground[r-1][c] for c in range(M)]

    for c in range(1, M):
        left[c] = max(left[c], left[c-1] + ground[r][c])
    for c in range(M-2, -1, -1):
        right[c] = max(right[c], right[c+1] + ground[r][c])

    for c in range(M):
        ground[r][c] = max(left[c], right[c])

print(ground[N-1][M-1])