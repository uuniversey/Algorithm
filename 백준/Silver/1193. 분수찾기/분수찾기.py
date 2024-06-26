X = int(input())
num = 1
while True:
    calc = X - num
    if calc > 0:
        X = calc
    else:
        break
    num += 1

if num % 2:
    print(f'{num - (X-1)}/{1 + (X-1)}')
else:
    print(f'{1 + (X - 1)}/{num - (X - 1)}')