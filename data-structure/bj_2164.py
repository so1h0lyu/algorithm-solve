import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque()

for i in range(1, n + 1):
    card.append(i)

i = 1
while (len(card) > 1):
    if (i % 2 == 0):
        card.append(card[0])
    card.popleft()

    i += 1
    
print(card[0])