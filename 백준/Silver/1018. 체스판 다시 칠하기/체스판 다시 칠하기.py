N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
k, l = 0, 0
min_v = float('inf')
num = 0
my_l = []
for i in range(N-7):
    for j in range(M-7):
        w = 0
        b = 0
        for r in range(i, 8+i):
            for c in range(j, 8+j):
                if (r+c) % 2:
                    if board[r][c] == 'W':
                        b += 1
                    else:
                        w += 1
                else:
                    if board[r][c] == 'W':
                        w += 1
                    else:
                        b += 1
        my_l.append(w)
        my_l.append(b)
print(min(my_l))