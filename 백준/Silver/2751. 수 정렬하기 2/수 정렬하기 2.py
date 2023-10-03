import sys
N = int(sys.stdin.readline())
li = []
for _ in range(N):
    n = int(sys.stdin.readline())
    li.append(n)
li.sort()
for l in li:
    print(l)