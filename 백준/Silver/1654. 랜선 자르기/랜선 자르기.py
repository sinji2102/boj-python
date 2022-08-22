import sys
input = sys.stdin.readline

K, N = map(int, input().split())

list_ = []

for i in range(K) :
    list_.append(int(input()))

start = 1
end = max(list_)

while start <= end :
    cnt = 0
    mid = (start + end) // 2

    for i in list_ :
        cnt += i // mid

    if cnt >= N :
        start = mid + 1
    else :
        end = mid - 1

print(end)


