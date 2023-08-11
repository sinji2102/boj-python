import sys

input = sys.stdin.readline

n = int(input().rstrip())
list_ = [0,1,2]

for i in range(2, n) :
    list_.append(list_[i]+list_[i-1])

print(list_[n]%10007)