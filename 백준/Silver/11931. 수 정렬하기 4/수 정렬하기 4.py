N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
for i in range(N):
    print(arr[i])