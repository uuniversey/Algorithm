from collections import deque

N = int(input())
card = deque(i+1 for i in range(N))
for _ in range(N-1):
    card.popleft()
    recy = card.popleft()
    card.append(recy)
print(card[0])