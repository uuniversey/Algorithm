import itertools

N, M = map(int, input().split())
sets = itertools.combinations([k for k in range(1, N+1)], M)
for se in sets:
    print(*se)