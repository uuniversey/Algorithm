import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().split()))
memo = [0] * (len(arr)+1)
memo[1] = arr[0]
for k in range(2, len(arr)+1):
    memo[k] = memo[k-1] + arr[k-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(memo[j] - memo[i-1])