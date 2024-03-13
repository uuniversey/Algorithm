import sys


def dfs(s, num):
    for v, i in Tree[s]:
        if not vstd[i]:
            vstd[i] = v+num
            dfs(i, vstd[i])


input = sys.stdin.readline
N = int(input())
Tree = [[] for _ in range(N+1)]
for _ in range(N):
    info = list(map(int, input().split()))
    i = 1
    while True:
        if info[i] == -1:
            break

        if info[0] > info[i]:
            Tree[info[0]].append((info[i+1], info[i]))
            Tree[info[i]].append((info[i+1], info[0]))

        i += 2

start = 0
for idx, val in enumerate(Tree):
    if len(val) == 1:
        start = idx
        break

vstd = [0] * (N+1)
vstd[start] = 1
dfs(start, 0)

START = vstd.index(max(vstd))
vstd = [0] * (N+1)
vstd[START] = 1
dfs(START, 0)

print(max(vstd))