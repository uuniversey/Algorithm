from collections import deque

N, K = map(int, input().split())
Belt = list(map(int, input().split()))
Belt = deque(Belt)

result = 1
robots = deque([0] * N)
while True:
    # 1
    Belt.rotate(1)
    robots.rotate(1)
    robots[N-1] = 0

    # 2
    for i in range(N-2, -1, -1):
        if robots[i] and robots[i+1] == 0 and Belt[i+1]:
            robots[i] = 0
            robots[i+1] = 1
            Belt[i+1] -= 1
    robots[N-1] = 0

    # 3
    if Belt[0] != 0:
        robots[0] = 1
        Belt[0] -= 1

    # 4
    num = Belt.count(0)
    if num >= K:
        break
    else:
        result += 1

print(result)