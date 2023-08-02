import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
list_ = []
price = []

for _  in range(M) :
    list_.append(int(input().rstrip()))

list_.sort()

for i in range(M) :
    if M-i <= N :
        price.append(list_[i] * (M-i))
    else :
        price.append(list_[i] * N)

print(list_[price.index(max(price))], max(price))