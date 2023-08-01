import sys

input = sys.stdin.readline
test_case = int(input().rstrip())

A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

A.sort()
B.sort()

answer = 0

for _ in range(test_case) :
    answer += A.pop(0) * B.pop(-1)

print(answer)