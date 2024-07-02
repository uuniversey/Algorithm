N = int(input())
M = int(input())
S = input()

pn = ''
for i in range(2*N+1):
    if i % 2:
        pn += 'O'
    else:
        pn += 'I'

ans = 0
for j in range(M):
    if pn == S[j:(j+2*N+1)]:
        ans += 1
print(ans)