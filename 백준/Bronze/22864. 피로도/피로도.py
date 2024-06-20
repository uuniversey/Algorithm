A, B, C, M = map(int, input().split())
battery, time, work = 0, 0, 0
while time <= 23:
    if A + battery > M:
        battery = max(battery-C, 0)
    else:
        battery += A
        work += B
    time += 1
print(work)