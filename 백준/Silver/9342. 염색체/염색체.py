import re

T = int(input())
pattern = re.compile(r'^[ABCDEF]?A+F+C+[ABCDEF]?$')

for _ in range(T):
    target = input().strip()
    if pattern.match(target):
        print('Infected!')
    else:
        print('Good')