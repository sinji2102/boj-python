import sys

input = sys.stdin.readline

n = int(input())
list_ = []
cnt = 1

for _ in range(n) :
    list_.append(int(input()))

right = list_[-1]

for i in range(len(list_)-1, -1, -1) :
    # print(i)
    if list_[i] > right :
        cnt +=1
        right = list_[i]

print(cnt)