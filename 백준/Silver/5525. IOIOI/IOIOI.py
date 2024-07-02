N = int(input())
M = int(input())
S = input()

ans = 0
i = 0
count = 0

while i < M-1:
    if S[i:i+3] == 'IOI':
        count += 1
        i += 2
        if count == N:
            ans += 1
            count -= 1
    else:
        i += 1
        count = 0

print(ans)