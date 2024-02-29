def perm(s, e):
    if s == e:
        print(*sets)
    else:
        for i in range(N):
            if not check[i]:
                check[i] = 1
                sets[s] = arr[i]
                perm(s+1, e)
                check[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sets = [0] * M
check = [0] * N
perm(0, M)