import sys

input = sys.stdin.readline

n = int(input().rstrip())
list_ = list(map(int, input().rstrip().split()))
cnt = list_.copy()

for i in range(1,n) :
    if cnt[i-1] > 0 :
        cnt[i] = cnt[i-1] + list_[i]
    else :
        pass

print(max(cnt))