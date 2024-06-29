import math
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = math.comb(M, N)
    print(ans)