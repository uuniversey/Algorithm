N = int(input())
ans = list(map(int, input().split()))
arr = [0] * (N+2)
res = 0

for i in range(N):
    if ans[i] != arr[i]:
        res += 1
        arr[i] = 1-arr[i]
        arr[i+1] = 1-arr[i+1]
        arr[i+2] = 1-arr[i+2]

print(res)