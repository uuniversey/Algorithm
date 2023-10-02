while True:
    s = input()
    if s == '0':
        break
    s_r = s[::-1]
    print('yes' if s == s_r else 'no')