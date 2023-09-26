T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    res = 0
    if N % H == 0:
        res = H * 100 + (N // H)
    else:
        res = (N % H) * 100 + (N // H) + 1

    print(res)