max_v = 0
res = 0
for i in range(9):
    j = int(input())
    if max_v < j:
        max_v = j
        res = i+1
print(max_v)
print(res)