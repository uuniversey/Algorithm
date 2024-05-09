N = int(input())
words = [input() for _ in range(N)]
words.sort()
res = []

for i in range(N):
    if i+1 < N and words[i+1].startswith(words[i]):
        continue
    res.append(words[i])

print(len(res))
