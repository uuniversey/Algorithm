import sys
N = int(input())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))
li.sort()
print(round(sum(li)/N))
print(li[N//2])
check = [0] * 8001
max_v = 0
for l in li:
    check[l+4000] += 1
    max_v = max(max_v, check[l+4000])
target = check.index(max_v)
check[target] = 0
try:
    print(check.index(max_v)-4000)
except ValueError:
    print(target-4000)
print(li[-1] - li[0])