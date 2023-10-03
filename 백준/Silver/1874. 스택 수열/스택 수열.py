import sys
n = int(input())
nums = [i+1 for i in range(n)]
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

std = []
res = []
stk = []
k = 0
num = 1
while num <= n:
    if not stk:
        stk.append(num)
        res.append('+')
    else:
        if arr[k] != stk[-1]:
            stk.append(num)
            res.append('+')
        else:
            res.append('-')
            std.append(stk.pop())
            k += 1
            num -= 1
    num += 1

while stk:
    std.append(stk.pop())
    res.append('-')

if std == arr:
    for r in res:
        print(r)

else:
    print('NO')