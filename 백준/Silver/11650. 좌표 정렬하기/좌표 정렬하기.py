N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append([x, y])

li.sort()
for l in li:
    print(*l)