H, W, N, M = map(int, input().split())

print(((H // (N+1)) + 1 if H % (N+1) != 0 else (H // (N+1))) * ((W // (M+1)) + 1 if W % (M+1) != 0 else (W // (M+1))))