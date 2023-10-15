def cut(n, p):
    global white, blue
    for k, l in [[p[0], p[1]], [p[0]+n, p[1]], [p[0], p[1]+n], [p[0]+n, p[1]+n]]:
        num = 0
        for i in range(k, n+k):
            for j in range(l, n+l):
                num += paper[i][j]

        if num == n ** 2:
            blue += 1

        elif num == 0:
            white += 1

        else:
            cut(n//2, [k, l])

        num = 0


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
test = 0

for r in range(N):
    test += sum(paper[r])

if test == 0:
    white += 1

elif test == N ** 2:
    blue += 1

else:
    cut(N//2, [0, 0])

print(white)
print(blue)