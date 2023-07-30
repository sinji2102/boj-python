import sys

input = sys.stdin.readline

test_case = int(input().rstrip())
tops = list(map(int, input().rstrip().split()))
stack = []
answer = []

for _ in range(test_case) :
    answer.append(0)

for i in range(test_case):
    while stack:
        if stack[-1][1] > tops[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tops[i]])

for j in answer :
    print(j, end = " ")