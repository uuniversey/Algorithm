import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = sys.maxsize

l, r = 0, N-1
while l < N and r >= 0:
    if l >= r:
        break
    calc = arr[l] + arr[r]
    if abs(calc) < abs(ans):
        ans = calc
        res = (arr[l], arr[r])

    if calc > 0:
        r -= 1
    elif calc < 0:
        l += 1
    else:
        break

print(*res)