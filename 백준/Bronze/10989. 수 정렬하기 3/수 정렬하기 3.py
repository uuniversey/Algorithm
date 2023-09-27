import sys

N = int(input())
check = [0] * 10000
for _ in range(N):
    check[int(sys.stdin.readline())-1] += 1

for i, v in enumerate(check):
    for j in range(v):
        print(i+1)