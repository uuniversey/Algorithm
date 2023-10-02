N = int(input())
A = set(input().split())
M = int(input())
M_A = input().split()
num = len(A)

for m in M_A:
    A.add(m)

    if len(A) != num:
        print('0')
        A.remove(m)
    else:
        print('1')