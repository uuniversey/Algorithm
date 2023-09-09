import copy


def make_sets(arr, a, n):

    if a == n:
        c_tool = copy.deepcopy(tool)
        subset.append(c_tool)

    else:
        for i in range(0, arr[a]):
            tool[a] = i
            make_sets(arr, a+1, n)


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]




li1 = [[1], [2], [3], [4]]
li2 = [[1, 3], [2, 4]]
li3 = [[1, 2], [2, 3], [3, 4], [4, 1]]
li4 = [[1, 2, 3], [2, 3, 4], [3, 4, 1], [4, 1, 2]]
li5 = [[1, 2, 3, 4]]
my_dic = {1: li1, 2: li2, 3: li3, 4: li4, 5: li5}

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
note = []
sets = []
cctv = []
subset = []

for row in range(N):
    for col in range(M):
        if office[row][col] != 0 and office[row][col] != 6:
            cctv.append(len(my_dic[office[row][col]]))
            for num in range(len(my_dic[office[row][col]])):
                li = my_dic[office[row][col]][num]         # [1, 3] 같은 녀석들
                tmp = []
                for e in li:
                    k = 1
                    while True:
                        ni = row + (di[e-1] * k)
                        nj = col + (dj[e-1] * k)
                        if 0 <= ni < N and 0 <= nj < M:
                            if office[ni][nj] == 6:
                                break
                            tmp.append([ni, nj])
                            k += 1
                        else:
                            break

                note.append(tmp)
            sets.append(note)
            note = []

tool = [0] * len(cctv)
make_sets(cctv, 0, len(cctv))
result = 1000

for s in subset:
    clone = copy.deepcopy(office)
    v = 0
    for idx, val in enumerate(s):
        for k in range(len(sets[idx][val])):
            clone[sets[idx][val][k][0]][sets[idx][val][k][1]] = 9
    for r in range(N):
        for c in range(M):
            if clone[r][c] == 0:
                v += 1

    result = min(result, v)

print(result)