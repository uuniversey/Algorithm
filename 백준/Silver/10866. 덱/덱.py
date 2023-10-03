import sys
from collections import deque

N = int(input())
deq = deque()
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_back':
        deq.append(int(order[1]))
    elif order[0] == 'push_front':
        deq.appendleft(int(order[1]))
    elif order[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif order[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif order[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])