import sys

input = sys.stdin.readline

N = int(input().rstrip())

list_ = [0 for _ in range(N+1)]

for i in range(2, N+1) :
    list_[i] = list_[i-1] + 1
    if i % 2 == 0 :
        list_[i] = min(list_[i], list_[i//2] + 1)
    if i % 3 == 0 : 
        list_[i] = min(list_[i], list_[i//3] + 1)

print(list_[N])