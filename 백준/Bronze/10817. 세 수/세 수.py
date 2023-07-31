import sys

input = sys.stdin.readline
list_ = list(map(int, input().rstrip().split()))

list_.sort()

print(list_[1])