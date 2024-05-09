import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_v = sys.maxsize
ans = []

for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        val = arr[i] + arr[left] + arr[right]
        if min_v > abs(val):
            min_v = abs(val)
            ans = [arr[i], arr[left], arr[right]]

        if val < 0:
            left += 1
        elif val > 0:
            right -= 1
        else:
            break
print(*ans)