import sys
N, M = map(int, input().split())
dic = {}
for i in range(N):
    dic[sys.stdin.readline().rstrip()] = i+1

r_dic = {v:k for k, v in dic.items()}

for j in range(M):
    data = sys.stdin.readline().rstrip()
    try:
        data = int(data)
    except:
        pass

    if type(data) == int:
        print(r_dic[data])

    else:
        print(dic[data])