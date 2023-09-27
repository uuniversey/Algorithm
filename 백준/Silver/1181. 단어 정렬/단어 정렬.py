N = int(input())
li = []
for _ in range(N):
    data = input()
    li.append((len(data), data))

li.sort()
li = list(set(li))

for i in li:
    print(i[1])