from math import floor


def flutter(d, p):    # 좌하우상

    f_delta = {
            0: [[-2, 0], [-1, -1], [-1, 0], [-1, 1], [0, -2], [1, -1], [1, 0], [1, 1], [2, 0], [0, -1]],
            1: [[0, -2], [1, -1], [0, -1], [-1, -1], [2, 0], [1, 1], [0, 1], [-1, 1], [0, 2], [1, 0]],
            2: [[2, 0], [1, 1], [1, 0], [1, -1], [0, 2], [-1, 1], [-1, 0], [-1, -1], [-2, 0], [0, 1]],
            3: [[0, 2], [-1, 1], [0, 1], [1, 1], [-2, 0], [-1, -1], [0, -1], [1, -1], [0, -2], [-1, 0]]
               }

    percent = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]

    i, j = p
    res = 0
    tmp = 0
    for idx, li in enumerate(f_delta[d]):
        di, dj = li
        if idx == 9:
            if 0 <= di+i < N and 0 <= dj + j < N:
                sands[di+i][dj+j] += sands[i][j] - tmp
            else:
                res += sands[i][j] - tmp

        else:
            if 0 <= di+i < N and 0 <= dj+j < N:
                sands[di+i][dj+j] += floor(percent[idx] * sands[i][j])

            else:
                res += floor(percent[idx] * sands[i][j])

            tmp += floor(percent[idx] * sands[i][j])

    sands[i][j] = 0
    return res


N = int(input())
sands = [list(map(int, input().split())) for _ in range(N)]
delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
sum_r = 0
ni, nj = N//2, N//2
D = []
num = 1

for m1 in range(N):
    for _ in range(num):
        D.append((2*m1) % 4)
    for _ in range(num):
        D.append((2*m1+1) % 4)
    num += 1

for n in range(N**2-1):
    d = D[n]
    ni += delta[d][0]
    nj += delta[d][1]
    sum_r += flutter(d, [ni, nj])

print(sum_r)