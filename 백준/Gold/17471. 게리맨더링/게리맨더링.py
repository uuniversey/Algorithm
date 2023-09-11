N = int(input())
arr = [a+1 for a in range(N)]
citizen = list(map(int, input().split()))
adj_l = [[] for _ in range(N+1)]
res = 1000000000

for k in range(1, N+1):
    adj_l[k] = list(map(int, input().split()))[1:]

for i in range(1, 1<<(N-1)):
    area_a = []
    area_b = []
    vstd_a = [0] * (N + 1)
    vstd_b = [0] * (N + 1)
    flag = 1
    for j in range(N):
        if i & (1<<j):
            area_a.append(arr[j])

    area_b = list(set(arr) - set(area_a))

    if len(area_a) == 1:
        pass
    else:
        for m in area_b:
            vstd_a[m] = 2

        q = [area_a[0]]
        while q:
            tmp = q.pop(0)
            for l in adj_l[tmp]:
                if vstd_a[l] == 0:
                    q.append(l)
                    vstd_a[l] = 1

        for c in area_a:
            if vstd_a[c] != 1:
                flag = 0
                break

    if len(area_b) == 1:
        pass
    else:
        for n in area_a:
            vstd_b[n] = 2

        q = [area_b[0]]
        while q:
            tmp = q.pop(0)
            for l in adj_l[tmp]:
                if vstd_b[l] == 0:
                    q.append(l)
                    vstd_b[l] = 1

        for d in area_b:
            if vstd_b[d] != 1:
                flag = 0
                break

    if flag == 1:
        for idx,val in enumerate(area_a):
             area_a[idx] = citizen[val-1]

        for idx,val in enumerate(area_b):
             area_b[idx] = citizen[val-1]

        res = min(res, abs(sum(area_a) - sum(area_b)))

if res == 1000000000:
    print(-1)
else:
    print(res)