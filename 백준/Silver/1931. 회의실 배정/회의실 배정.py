import sys
N = int(input())
time = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time.append((e, s))

time.sort()
res = [time[0]]
num = 1
for t in range(1, N):
    if time[t][1] >= res[-1][0]:
        res.append(time[t])
        num += 1

print(num)