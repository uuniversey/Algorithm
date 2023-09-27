while True:
    a, b, c = map(int, input().split())
    if a+b+c == 0:
        break
    A, B, C = sorted([a, b, c])
    print('right' if A**2 + B**2 == C**2 else 'wrong')