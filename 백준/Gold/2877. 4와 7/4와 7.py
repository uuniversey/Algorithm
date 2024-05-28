K = int(input())
num = bin(K+1)[2:][1:]
res = ''
for n in num:
    if n == '0':
        res += '4'
    else:
        res += '7'
print(res)