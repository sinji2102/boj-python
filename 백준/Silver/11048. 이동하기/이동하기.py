import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
list_ = []
cnt = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N) :
    list_.append(list(map(int, input().rstrip().split())))

for i in range(N):
    for j in range(M) :
        if i != 0 and j != 0 : 
            cnt[i][j] = max(cnt[i-1][j], cnt[i][j-1], cnt[i-1][j-1]) + list_[i][j]
        elif i != 0 :
            cnt[i][j] = cnt[i-1][j] + list_[i][j]
        elif j != 0 :
            cnt[i][j] = cnt[i][j-1] + list_[i][j]
        else :
            cnt[i][j] = list_[i][j]
        
        # print(cnt)

print(cnt[N-1][M-1])

