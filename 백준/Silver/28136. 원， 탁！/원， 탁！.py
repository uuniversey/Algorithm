N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    if arr[i] <= arr[i-1]:
        ans += 1

if arr[-1] >= arr[0]:
    ans += 1
print(ans)