from math import sqrt


def z(n, r, c, p):
    x = sqrt(n)
    if n == 1:
        print(p[0])
        exit()
        return
    else:
        if r < (x//2):
            if c < (x//2):  # 1
                z(n//4, r, c, (p[0], n//4))
            else:           # 3
                z(n//4, r, c-x//2, (p[0] + n//4, p[1] + 2*(n//4)))
        else:
            if c < (x//2):  # 2
                z(n//4, r-x//2, c, (p[0] + 2*(n//4), p[1] + n-n//4))
            else:           # 4
                z(n//4, r-x//2, c-x//2, (p[0] + n-n//4, p[1]))


N, r, c = map(int, input().split())
z(2**(2*N), r, c, (0, 2**(2*N)))