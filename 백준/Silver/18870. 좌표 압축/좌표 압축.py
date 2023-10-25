N = int(input())
arr = list(map(int, input().split()))
arr3 = sorted(set(arr))
dic = {}
k = 0
for a3 in arr3:
    dic[a3] = k
    k += 1
for a in arr:
    print(dic[a], end=' ')
