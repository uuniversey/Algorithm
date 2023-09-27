N = int(input())
grade = list(map(int, input().split()))
tool = max(grade)
res = 0
cnt = 0
for g in grade:
    res += (g / tool) * 100
    cnt += 1

print(res / cnt)