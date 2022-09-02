import sys
from collections import Counter

input = sys.stdin.readline

test_c = int(input())

list_ = []
for i in range(test_c) :
    list_.append(int(input().rstrip()))

# 산술평균
sum = 0
for i in list_ :
    sum += i
print(round(sum/test_c))

# 중앙값
list_.sort()
print(list_[test_c//2])

# 최빈값 >> 이게 개어려운디.....

cnt = Counter(list_).most_common(2) # 빈도수가 높은 수 2개 가져오기

if len(list_) > 1 : # list_의 길이가 1보다 크면
    if cnt[0][1] == cnt[1][1] : # 최빈값이 2개 이상이면
        print(cnt[1][0])    # 2번째 거 가져오기
    else : print(cnt[0][0]) # 아니면 첫번째 거 가져오기
else : print(cnt[0][0]) # 하나면 그냥 그거 가져오기

# 범위
print(list_[-1]-list_[0])