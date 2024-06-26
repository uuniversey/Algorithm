def toggle(n):
    if n:
        return 0
    else:
        return 1


N = int(input())
ans = list(map(int, input().split()))
arr = [0] * N
res = 0

for i in range(N):
    if ans[i] != arr[i]:
        res += 1
        arr[i] = toggle(arr[i])
        try:
            arr[i+1] = toggle(arr[i+1])
        except:
            continue
        try:
            arr[i+2] = toggle(arr[i+2])
        except:
            continue

print(res)