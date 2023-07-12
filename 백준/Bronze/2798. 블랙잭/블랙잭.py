import sys

input = sys.stdin.readline

cnt, M = map(int, input().split())

list_ = list(map(int, input().split()))

max_num = 0

for i in range(len(list_) - 2):
    for j in range(i + 1, len(list_) - 1):
        for k in range(j + 1, len(list_)):
            sum = list_[i] + list_[j] + list_[k]	# 세 숫자 더함
            if sum <= M:				# M보다 작은 가장 큰 수를 max_num에 대입
                max_num = max(max_num, sum)
                
print(max_num)