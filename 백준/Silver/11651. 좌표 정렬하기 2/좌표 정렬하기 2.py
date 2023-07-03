import sys

input = sys.stdin.readline

test_case = int(input())

list_ = []

for i in range(test_case):
    x, y = map(int, input().split())
    list_.append((x,y))

list_.sort(key = lambda x:x[0])
list_.sort(key = lambda x:x[1])

for j in range(test_case):
    print(list_[j][0], list_[j][1])