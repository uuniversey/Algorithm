def combi(s, k, e):
    global sum_v, res

    if s == e:
        if M - sum(sets) >= 0:
            if sum_v > M-sum(sets):
                sum_v = M-sum(sets)
                res = sum(sets)

    else:
        for i in range(k, N):
            sets[s] = card[i]
            combi(s+1, i+1, e)


N, M = map(int, input().split())
card = list(map(int, input().split()))
sets = [0] * 3
sum_v = 300000
res = 0

combi(0, 0, 3)
print(res)