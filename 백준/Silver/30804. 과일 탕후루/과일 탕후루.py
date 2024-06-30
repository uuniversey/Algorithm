N = int(input())
fruits = list(map(int, input().split()))

ans = 0
left = 0
memo = {}

for right in range(N):
    fruit = fruits[right]
    if fruit in memo:
        memo[fruit] += 1
    else:
        memo[fruit] = 1

    while len(memo) > 2:
        memo[fruits[left]] -= 1
        if memo[fruits[left]] == 0:
            del memo[fruits[left]]
        left += 1

    ans = max(ans, right-left+1)

print(ans)