import sys

input = sys.stdin.readline
test_case = int(input().rstrip())
list_ = [0] * 10001

for _ in range(test_case) :
    list_[int(input())] += 1

for i in range(10001) :
    if list_[i] != 0 :
        for j in range(list_[i]) :
            print(i)
