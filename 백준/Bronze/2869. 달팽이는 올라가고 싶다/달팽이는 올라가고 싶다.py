A, B, V = map(int, input().split())
if A == V:
    print(1)
else:
    if not (V-A) % (A-B):
        print((V-A) // (A-B) + 1)
    else:
        print((V-A) // (A-B) + 2)