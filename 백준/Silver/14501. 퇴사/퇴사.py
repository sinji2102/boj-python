import sys

input = sys.stdin.readline

N = int(input().rstrip())
list_ = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = [0 for _ in range(N+1)]

for i in range(N) :
    for j in range(i + list_[i][0], N+1) :
        if cnt[j] < cnt[i] + list_[i][1] :
            cnt[j] = cnt[i] + list_[i][1]

print(cnt[-1])