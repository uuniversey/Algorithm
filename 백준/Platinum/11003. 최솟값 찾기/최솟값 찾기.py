import sys
from collections import deque

input = sys.stdin.readline
N, L = map(int, input().split())
arr = list(map(int, input().split()))
stage = deque()

for i in range(N):
    while stage and stage[-1][1] >= arr[i]:
        stage.pop()

    stage.append((i+1, arr[i]))

    while stage[0][0] < (i-L+2):
        stage.popleft()

    print(stage[0][1], end=" ")