T = int(input())
for _ in range(T):
    n = int(input())

    th = n // 3
    num = 0
    ans = []
    while th >= 0:
        num = n - (th * 3)
        ans.append(num//2)
        th -= 1

    print(sum(ans) + len(ans))