N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append((y, x))

li.sort()
for l in li:
    a, b = l
    print(b, a)