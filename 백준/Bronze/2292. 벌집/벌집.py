N = int(input())
li = []
for n in range(18500):
    li.append(1+(3*n)*(n+1))

for i, v in enumerate(li):
    if N <= v:
        print(i+1)
        break