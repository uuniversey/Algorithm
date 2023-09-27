N = int(input())
sol = [0] * N
for i in range(1, N+1):
    sum_v = 0
    for j in list(str(i)):
        sum_v += int(j)
    sum_v += i
    sol[i-1] = sum_v

try:
    print(sol.index(N)+1)
except ValueError:
    print(0)