K = int(input())
stk = []
for _ in range(K):
    k = int(input())
    if k == 0:
        stk.pop()
    else:
        stk.append(k)
print(sum(stk))