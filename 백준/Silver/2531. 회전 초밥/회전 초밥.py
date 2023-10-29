from collections import deque
import sys
N, d, k, c = map(int, input().split())
li = [int(sys.stdin.readline()) for _ in range(N)]
first = [li[i] for i in range(k)]
li += first
dq = deque(first)
res = 0
for j in range(N):
    calc = 0
    if not c in dq:
        calc += 1
    calc += len(list(set(dq)))
    res = max(res, calc)
    dq.popleft()
    dq.append(li[k])
    k += 1
print(res)