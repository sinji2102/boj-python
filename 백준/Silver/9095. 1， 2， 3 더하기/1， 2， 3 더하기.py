import sys

input = sys.stdin.readline

test_case = int(input().rstrip())
list_ = [0,1,2,4]

for i in range(3, 12) :
    list_.append(list_[i]+list_[i-1]+list_[i-2])

for _ in range(test_case) :
    n = int(input().rstrip())

    print(list_[n])