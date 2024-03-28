import sys
input = sys.stdin.readline
N = int(input())
cave = []

for _ in range(N):
    k, *arr = input().split()
    cave.append(arr)
cave.sort()

check = []
for c in cave:
    for idx, val in enumerate(c):
        if c[:idx+1] in check:
            continue
        print('--' * idx + val)
        check.append(c[:idx+1])