import sys

input = sys.stdin.readline
list_ = list(map(int, input().rstrip()))

list_.sort(reverse=True)

for i in list_ :
    print(i,end="")