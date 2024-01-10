N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
seat = [[0] * N for _ in range(N)]
seq = [students[0][0]]

seat[1][1] = students[0][0]
for i in range(1, N**2):
    seq.append(students[i][0])

    info = []
    for r in range(N):
        for c in range(N):
            goto = 0
            empty = 0
            if not seat[r][c]:
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if seat[nr][nc] in students[i][1:5]:
                            goto += 1
                        elif not seat[nr][nc]:
                            empty += 1
                info.append([goto, empty, [r, c]])

    info.sort(reverse=True)
    n = len(info)
    if not n:
        break
    elif n == 1:
        seat[info[0][2][0]][info[0][2][1]] = students[i][0]
    else:
        k = 0
        while n > k:
            if k == n-1:
                seat[info[-1][2][0]][info[-1][2][1]] = students[i][0]
                break

            if info[k][0] != info[k+1][0]:
                seat[info[k][2][0]][info[k][2][1]] = students[i][0]
                break

            if info[k][1] != info[k+1][1]:
                seat[info[k][2][0]][info[k][2][1]] = students[i][0]
                break

            k += 1

res = 0
for r1 in range(N):
    for c1 in range(N):
        for j in range(len(seq)):
            if seq[j] == seat[r1][c1]:
                tmp = j

        goto1 = 0
        for dr1, dc1 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr1, nc1 = r1 + dr1, c1 + dc1
            if 0 <= nr1 < N and 0 <= nc1 < N:
                if seat[nr1][nc1] in students[tmp][1:5]:
                    goto1 += 1

        if goto1 == 0:
            pass
        else:
            res += 10**(goto1-1)

print(res)