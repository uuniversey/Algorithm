N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

res = float('inf')
arr = [k+1 for k in range(N)]
for m in range(1, (1<<N)//2):
    s_team = set()
    for n in range(N):
        if m & (1<<n):
            s_team.add(arr[n])

    l_team = set(arr).difference(s_team)

    s_sum = 0
    l_sum = 0
    for s1 in s_team:
        for s2 in s_team:
            s_sum += ability[s1-1][s2-1]

    for l1 in l_team:
        for l2 in l_team:
            l_sum += ability[l1-1][l2-1]

    mysum = abs(s_sum - l_sum)

    res = min(res, mysum)

print(res)