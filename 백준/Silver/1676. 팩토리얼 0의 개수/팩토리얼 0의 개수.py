N = int(input())
num = 1
for i in range(N):
    num *= (i+1)

for idx, val in enumerate(str(num)[::-1]):
    if val != '0':
        print(idx)
        break