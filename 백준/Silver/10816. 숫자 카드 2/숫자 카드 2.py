N = int(input())
card = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))

check = [0] * 20000001
for n in card:
    check[n + 10000000] += 1

for m in test:
    print(check[m + 10000000], end=' ')