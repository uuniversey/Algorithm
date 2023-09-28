N = int(input())
nums = map(int, input().split())
check = [i+1 for i in range(1, 1000)]

for j in range(2, 1000):
    for k in check:
        if k != j and k % j == 0:
            check.remove(k)

cnt = 0
for n in nums:
    if n in check:
        cnt += 1

print(cnt)