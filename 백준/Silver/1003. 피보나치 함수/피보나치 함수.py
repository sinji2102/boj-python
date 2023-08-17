import sys


input = sys.stdin.readline

test_case = int(input().rstrip())
list_ = []

for i in range(41) :
    if i == 0 :
        list_.append([1, 0])
    elif i == 1 :
        list_.append([0, 1])
    else :
        list_.append([list_[i-2][0] + list_[i-1][0], list_[i-2][1] + list_[i-1][1]])

for _ in range(test_case) :
    N = int(input().rstrip())
    print(list_[N][0], list_[N][1]) 