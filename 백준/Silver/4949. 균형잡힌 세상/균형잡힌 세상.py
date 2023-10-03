import sys
while True:
    flag = 0
    arr = list(sys.stdin.readline().rstrip())
    if arr == ['.']:
        break
    stk = []
    for a in arr:
        if a == '(' or a == '[':
            stk.append(a)

        if stk:
            if a == ')':
                if stk[-1] == '(':
                    stk.pop()
                else:
                    flag = 1
                    break

            elif a == ']':
                if stk[-1] == '[':
                    stk.pop()
                else:
                    flag = 1
                    break

        else:
            if a == ')' or a == ']':
                flag = 1

    if not stk:
        pass
    else:
        flag = 1

    if flag:
        print('no')
    else:
        print('yes')