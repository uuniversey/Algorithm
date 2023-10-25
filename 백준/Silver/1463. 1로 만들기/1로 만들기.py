from collections import deque

n = int(input())
dq = deque()
dq.append([0, n])
vt = [0] * (n+1)
while dq:
    r, p = dq.popleft()

    if p == 1:
        print(r)
        break

    if p % 3 == 0 and vt[p] == 0:
        dq.append([r+1, p//3])

    if p % 2 == 0 and vt[p] == 0:
        dq.append([r+1, p//2])

    vt[p] = 1
    dq.append([r+1, p-1])