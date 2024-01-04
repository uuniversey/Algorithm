def solution(s, skip, index):
    
    alpabet = 'abcdefghijklmnopqrstuvwxyz'
    for elem in skip:
        if elem in alpabet:
            alpabet = alpabet.replace(elem, '')
    
    alpabet *= 10
    my_str = list(s)
    
    for i in range(len(s)):
        my_idx = alpabet.index(s[i]) + index
        my_str[i] = alpabet[my_idx]
    
    result = ''
    for m in my_str:
        result += m
        
    answer = result
    return answer