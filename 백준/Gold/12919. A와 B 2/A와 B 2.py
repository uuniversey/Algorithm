S = input()
ans = input()

q = [ans]
while q:
    myS = q.pop(0)
    if len(myS) == len(S) and myS == S:
        print(1)
        exit()

    if myS[-1] == 'A' and len(myS) > len(S):
        q.append(myS[:-1])

    revS = myS[::-1]
    if revS[-1] == 'B' and len(myS) > len(S):
        q.append(revS[:-1])

print(0)