T = int(input())
for _ in range(T):
    stack = []
    li = list(input())
    for i in li:
        if i == '(':
            if stack:
                if stack[-1] == i:
                    stack.append(i)
            else:
                stack.append(i)

        else:
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')