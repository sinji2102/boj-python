import sys

input = sys.stdin.readline

test_c = int(input().strip())
list_ = []

for i in range(test_c) :
    n = int(input().strip())
    list_.append(n)

list_.sort()

for j in list_ :
    print(j)