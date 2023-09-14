def cleaning(s, delta, d):
    global clean
    sign = 0
    if room[s[0]][s[1]] == 0:
        room[s[0]][s[1]] = 9
        clean += 1

    for e in delta:
        ni, nj = s[0]+e[0], s[1]+e[1]
        if room[ni][nj] == 0:
            sign = 1

    if sign:    # 3번
        d = (d + 3) % 4
        s[0] += delta[d][0]
        s[1] += delta[d][1]
        if room[s[0]][s[1]] == 0:
            cleaning(s, delta, d)
        else:
            s[0] -= delta[d][0]
            s[1] -= delta[d][1]
            cleaning(s, delta, d)

    else:   # 2번
        s[0] += delta[(d + 2) % 4][0]
        s[1] += delta[(d + 2) % 4][1]

        if room[s[0]][s[1]] == 1:
            return clean
        else:
            cleaning(s, delta, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
clean = 0

cleaning([r, c], delta, d)
print(clean)