arr = list(input())
li = [0] * 26

for i in arr:
    li[ord(i)-65] += 1

ans = ''
check = ''
for j in range(25, -1, -1):
    alpa = chr(j+65)
    while li[j] >= 2:
        ans += alpa
        ans = alpa + ans
        li[j] -= 2

    if li[j]:
        if check:
            print("I'm Sorry Hansoo")
            exit()
        else:
            check = alpa

n = len(ans) // 2
print(ans[0:n] + check + ans[n:])