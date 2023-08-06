import sys

input = sys.stdin.readline
test_case = int(input().rstrip())
tip = []
cnt = 0

for _ in range(test_case) :
    tip.append(int(input().rstrip()))

tip.sort(reverse=True)

for i in range(test_case) :
    if tip[i] - i > 0 :
        cnt += tip[i] - i
        # print("cnt:",cnt)

print(cnt)
