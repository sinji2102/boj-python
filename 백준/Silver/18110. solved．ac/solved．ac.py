import sys

input = sys.stdin.readline

test_case = int(input())

# 0 넣으면 ZeroDivisionError남
if not test_case:
    print(0)
    exit()

list_ = [int(input()) for _ in range(test_case)]

list_.sort()

p = int(test_case * 3 / 20 + 0.5)

# for i in range(p):
#     del list_[len(list_)-1]
#     del list_[0]
if p : 
    list_ = list_[p : -p]


ans = (sum(list_)/(len(list_)))

print(int(ans + 0.5))