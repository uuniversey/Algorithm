T = int(input())
for t in range(1, T+1):
    R, S = input().split()
    S = list(S)
    r = ''
    for s in S:
        r += s * int(R)

    print(r)