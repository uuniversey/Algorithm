N = int(input())
li = []
for i in range(2666800):
    if '666' in str(i):
        li.append(i)

print(li[N-1])