N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

t = 0
for s in size:
    if s != 0:
        if s%T:
            t += (s//T + 1)
        else:
            t += s//T

print(t)
print(N//P, N%P)