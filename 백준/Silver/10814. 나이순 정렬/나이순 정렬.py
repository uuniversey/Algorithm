N = int(input())
li = []
num = 0
for _ in range(N):
    age, name = input().split()
    li.append((int(age), num, name))
    num += 1
li.sort()

for l in li:
    print(int(l[0]), l[2])