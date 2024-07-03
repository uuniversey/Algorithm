T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    k = x
    flag = False
    while k <= M * N:
        if (k-1) % N + 1 == y:
            print(k)
            flag = True
            break
        k += M

    if not flag:
        print(-1)