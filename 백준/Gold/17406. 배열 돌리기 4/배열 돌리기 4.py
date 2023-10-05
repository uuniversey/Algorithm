import copy


def perm(s, e):
    global arr
    global min_v
    if s == e:
        for set in sets:
            r1, c1, s1 = order[set]
            rot(r1-1, c1-1, s1)

        for a in arr:
            min_v = min(min_v, sum(a))

        arr = copy.deepcopy(c_arr)
        return
    else:
        for i in range(K):
            if check[i] == 0:
                check[i] = 1
                sets[s] = p_arr[i]
                perm(s+1, e)
                check[i] = 0


def rot(r, c, s):
    while s != 0:
        idx = [[r-s, c-s+k1] for k1 in range(2*s + 1)] + [[r-s+k2, c+s] for k2 in range(1, 2*s)] + [[r+s, c+s-k3] for k3 in range(2*s + 1)] + [[r+s-k4, c-s] for k4 in range(1, 2*s)]
        li = []
        for dr, dc in idx:
            li.append(arr[dr][dc])
        tmp = li.pop()
        li.insert(0, tmp)

        n = 0
        for nr, nc in idx:
            arr[nr][nc] = li[n]
            n += 1

        s -= 1


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
c_arr = copy.deepcopy(arr)
order = []
for _ in range(K):
    r, c, s = map(int, input().split())
    order.append((r, c, s))

p_arr = [j for j in range(K)]
sets = [0] * K
check = [0] * K
min_v = 5001
perm(0, K)

print(min_v)