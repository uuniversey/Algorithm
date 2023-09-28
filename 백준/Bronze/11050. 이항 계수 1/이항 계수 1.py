N, K = map(int, input().split())

m, s = 1, 1
for i in range(K):
    m *= N
    s *= K-i
    N -= 1
    
print(m//s)