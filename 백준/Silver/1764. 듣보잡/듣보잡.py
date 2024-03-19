import sys
N, M = map(int, input().split())
dic = {}

for _ in range(N+M):
    name = sys.stdin.readline().rstrip()
    if dic.get(name) is None:
        dic[name] = 0
    else:
        dic[name] += 1

li = []
for d in dic:
    if dic[d]:
        li.append(d)

li.sort()
print(len(li))
for l in li:
    print(l)