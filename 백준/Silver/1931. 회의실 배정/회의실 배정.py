import sys

input = sys.stdin.readline
test_case = int(input().rstrip())
list_ = []
cnt = 0
lastIdx = 0

for _ in range(test_case) :
    list_.append(list(map(int, input().rstrip().split())))

# 회의 끝나는 시간을 우선으로 정렬해야 함 !!
list_.sort(key=lambda x : (x[1], x[0]))
# print(list_)

for i in range(test_case) :
    # list_[0][1]부터 시작하는 게 아니라 0부터 시작해야 함
    #   >> 맨 처음 것도 카운트하기 위해서
    if list_[i][0] >= lastIdx :
        cnt += 1
        lastIdx = list_[i][1]

print(cnt)
