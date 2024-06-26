N, K = map(int, input().split())
pixel = [list(map(int, input().split())) for _ in range(N)]
ans = []

for pix in pixel:
    tmp = []
    for p in pix:
        for i in range(K):
            tmp.append(p)
    for j in range(K):
        print(*tmp)