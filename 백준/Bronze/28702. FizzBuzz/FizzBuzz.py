strs = [input() for _ in range(3)]

for idx, val in enumerate(strs):
    try:
        num = int(val)
    except ValueError:
        continue

    if idx == 0:
        ans = num + 3
        break
    elif idx == 1:
        ans = num + 2
        break
    else:
        ans = num + 1
        break

if ans % 3:
    if ans % 5:
        print(ans)
    else:
        print('Buzz')
else:
    if ans % 5:
        print('Fizz')
    else:
        print('FizzBuzz')