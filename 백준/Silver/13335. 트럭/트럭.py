from collections import deque

n, w, L = map(int, input().split())
truck = deque(list(map(int, input().split())))
bridge = deque([0] * w)
t = 0
while True:
    t += 1
    cand = truck.popleft()

    if sum(bridge) + cand <= L:
        bridge[0] = cand
    else:
        truck.appendleft(cand)

    if bridge[-1]:
        bridge[-1] = 0

    bridge.rotate(1)

    if not truck:
        break

print(t + w)