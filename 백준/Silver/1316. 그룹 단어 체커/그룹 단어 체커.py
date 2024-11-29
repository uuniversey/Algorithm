N = int(input())
words = [input() for _ in range(N)]
ans = 0

for word in words:
    dic = {}
    memo = word[0]
    for w in word:
        if not dic.get(w):
            dic[w] = 1
        else:
            if memo != w:
                break
        memo = w

    else:
        ans += 1

print(ans)