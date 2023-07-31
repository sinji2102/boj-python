import sys

input = sys.stdin.readline
test_case = int(input().rstrip())

list_ = []

for _ in range(test_case) :
    list_.append(int(input().rstrip()))

list_.sort()

for i in list_ :
    print(i)