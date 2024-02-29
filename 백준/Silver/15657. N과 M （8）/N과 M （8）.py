def comb(s, k, e):
    if s == e:
        print(*sets)
    else:
        for i in range(k, N):
            sets[s] = arr[i]
            comb(s+1, i, e)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sets = [0] * M
comb(0, 0, M)