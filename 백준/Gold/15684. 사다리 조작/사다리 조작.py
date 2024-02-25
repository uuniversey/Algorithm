import sys


def check(a, b):
    start = b
    while a != H:
        if ladder[a][b] == -1:
            b += 1
            a += 1
        elif ladder[a][b] == 0:
            b -= 1
            a += 1
        else:
            a += 1

    if b != start:
        return False
    else:
        return True


def comb(s, k, e):
    if s == e:
        tmp = []
        for se in sets:
            x, y = se
            if ladder[x][y] != 1:
                for t in tmp:
                    a, b = t
                    ladder[a][b] = 1
                    ladder[a][b + 1] = 1
                return
            tmp.append(se)
            ladder[x][y] = -1
            ladder[x][y+1] = 0

        ischeck = True
        for j in range(N):
            ischeck = check(0, j)
            if not ischeck:
                break

        if ischeck == True:
            print(res)
            exit()

        for t in tmp:
            a, b = t
            ladder[a][b] = 1
            ladder[a][b+1] = 1

    else:
        for i in range(k, len(cand)):
            sets[s] = cand[i]
            comb(s+1, i+1, e)


input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[1] * N for _ in range(H)]

impossible = []
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = -1
    ladder[a-1][b] = 0
    impossible.append((a-1, b-1))
    impossible.append((a-1, b))
    if b-2 >= 0:
        impossible.append((a-1, b-2))

cand = []
for r in range(H):
    for c in range(N-1):
        if not (r, c) in impossible:
            cand.append((r, c))

res = 0
ischeck = True
for k in range(N):
   ischeck = check(0, k)
   if not ischeck:
       break
else:
    print(res)
    exit()
res += 1

while res < 4:
    sets = [0] * res
    comb(0, 0, res)
    res += 1
print(-1)