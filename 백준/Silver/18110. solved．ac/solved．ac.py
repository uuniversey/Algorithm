import sys
n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()
num = int(n * 0.15 + 0.5)
for i in range(num):
    li[i] = 0
    li[-i-1] = 0

try:
    print(int(sum(li)/(len(li) - num * 2) + 0.5))
except ZeroDivisionError:
    print(0)