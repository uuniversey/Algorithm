n = int(input())
if n == 1:
    print(1)
else:
    res = [0] * (n + 1)
    res[1], res[2] = 1, 2
    for i in range(3, n+1):
        res[i] = res[i-2] + res[i-1]

    print(res[n] % 10007)