from collections import deque
import sys
li = list(sys.stdin.readline().rstrip())
n1, n2 = li.count('a'), len(li)
standard = deque(['a' for i in range(n1)] + ['b' for j in range(n2-n1)])
res = 1000000
for k in range(n2):
    calc = 0
    standard.rotate(1)
    for l in range(n2):
        if li[l] != standard[l]:
            calc += 1

    res = min(res, calc)

print(res//2)