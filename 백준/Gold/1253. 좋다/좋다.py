def bs(t, s, e):
    while(s < e):
        if s == t:
            s += 1
            continue
        elif e == t:
            e -= 1
            continue

        if arr[s]+arr[e] < arr[t]:
            s += 1
        elif arr[s]+arr[e] > arr[t]:
            e -= 1
        else:
            return True

N = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0

for i in range(N):
    if bs(i, 0, N-1) == True:
        ans += 1

print(ans)