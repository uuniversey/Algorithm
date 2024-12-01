def solution(arr):
    answer = 1
    n = len(arr)

    for r in range(n):
        for c in range(r, n):
            if arr[r][c] != arr[c][r]:
                answer = 0
                
    return answer
