import sys

input = sys.stdin.readline
test_case = int(input().rstrip())
list_ = list(map(int, input().rstrip().split()))
answer1 = 0
answer2 = 0

list_.sort()

for i in list_ :
    answer1 += i
    answer2 += answer1

print(answer2)