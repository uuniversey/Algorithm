N = int(input())
grid = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dic = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
    boxes = [[x, y]]
    boxes.append([(x+dic[d][0]), (y+dic[d][1])])

    while g != 0:
        o = boxes[-1]
        for idx in range(len(boxes)-2, -1, -1):
            t = [boxes[idx][0], boxes[idx][1]]
            x = abs(o[0] - t[0])
            y = abs(o[1] - t[1])

            if o[0] < t[0] and o[1] < t[1]:     #1
                boxes.append([o[0] - y, o[1] + x])

            elif o[0] > t[0] and o[1] < t[1]:   #2
                boxes.append([o[0] - y, o[1] - x])

            elif o[0] > t[0] and o[1] > t[1]:   #3
                boxes.append([o[0] + y, o[1] - x])

            elif o[0] < t[0] and o[1] > t[1]:   #4
                boxes.append([o[0] + y, o[1] + x])

            else:
                if x == 0 and y != 0:
                    boxes.append([o[0]+(o[1]-t[1]), o[1]])
                elif y == 0 and x != 0:
                    boxes.append([o[0], o[1]-(o[0]-t[0])])
                else:
                    pass

        g -= 1

    for i in range(len(boxes)):
        grid[boxes[i][0]][boxes[i][1]] = 1

res = 0
for r in range(100):
    for c in range(100):
        if grid[r][c] and grid[r+1][c] and grid[r][c+1] and grid[r+1][c+1]:
            res += 1

print(res)