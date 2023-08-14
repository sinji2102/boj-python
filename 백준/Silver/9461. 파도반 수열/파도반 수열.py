import sys

input = sys.stdin.readline

test_case = int(input().rstrip())

for _ in range(test_case) :
    list_ = [0,1,1,1]
    N = int(input().rstrip())
    for i in range(4, N+1) :
        list_.append(list_[i-3]+list_[i-2])
    print(list_[-1])