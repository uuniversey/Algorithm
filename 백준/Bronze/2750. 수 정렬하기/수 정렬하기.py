N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()
[print(li[i]) for i in range(N)]