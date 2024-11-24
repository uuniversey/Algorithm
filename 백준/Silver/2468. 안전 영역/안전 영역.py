N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
safety = [[0] * N for _ in range(N)]
ans = 0

for rain in range(101):
    vstd = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if safety[r][c] == 0 and area[r][c] <= rain:
                safety[r][c] = 1

    cnt = 0
    for r1 in range(N):
        for c1 in range(N):
            if vstd[r1][c1] == 0 and safety[r1][c1] == 0:
                cnt += 1
                vstd[r1][c1] = 1
                q = [(r1, c1)]
                while q:
                    nr, nc = q.pop()
                    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        R, C = nr+dr, nc+dc
                        if 0 <= R < N and 0 <= C < N and vstd[R][C] == 0 and safety[R][C] == 0:
                            vstd[R][C] = 1
                            q.append((R, C))
    ans = max(cnt, ans)

print(ans)
