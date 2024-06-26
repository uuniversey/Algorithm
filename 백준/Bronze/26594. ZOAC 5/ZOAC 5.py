arr = input()
num = 0
memo = arr[0]
for a in arr:
    if memo != a:
        break
    num += 1

print(num)