N, M = map(int, input().split())


def per(s, e):
    if s == e:
        print(*sets)
        return

    else:
        for j in range(N):
            if check[j] == 0:
                check[j] = 1
                sets[s] = arr[j]
                per(s+1, e)
                check[j] = 0


arr = [i for i in range(1, N+1)]
sets = [0] * M
check = [0] * N
per(0, M)