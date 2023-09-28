N, K = map(int, input().split())
li = [i+1 for i in range(N)]
p = -1

print('<', end='')
for j in range(N):
    if len(li) != 1:
        idx = (p+K) % len(li)
        num = li.pop(idx)
        print(num, end=', ')
        p = idx-1
    else:
        print(li.pop(p), end='')
        print('>')