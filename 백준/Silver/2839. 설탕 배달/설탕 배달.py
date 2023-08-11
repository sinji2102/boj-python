import sys

input = sys.stdin.readline

N = int(input().rstrip())

list_ = [-1 for _ in range(5001)]

list_[3] = 1
list_[5] = 1

for i in range(6, N+1) :
    if list_[i-3] < 0 and list_[i-5] < 0:
        list_[i] = -1

    elif list_[i-3] > 0 and list_[i-5] > 0 :
        list_[i] = min(list_[i-3], list_[i-5]) + 1

    else :
        # -1이 들어가면 안 되므로 max로 계산!!
        list_[i] = max(list_[i-3], list_[i-5]) + 1

print(list_[N])

