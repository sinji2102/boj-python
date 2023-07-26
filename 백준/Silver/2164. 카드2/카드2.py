import sys
from collections import deque

test_case = int(sys.stdin.readline().rstrip())
cards = deque()

for i in range(1, test_case+1) :
    cards.append(i)

while len(cards) > 1:

    cards.popleft()
    cards.append(cards.popleft())

    # print(cards)

print(cards[0])
