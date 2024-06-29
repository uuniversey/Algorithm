N = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
arr_A.sort(reverse=True)
arr_B.sort()

S = 0
for idx, val in enumerate(arr_A):
    S += val * arr_B[idx]
print(S)