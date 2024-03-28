import sys

input = sys.stdin.readline

N = int(input().rstrip())
N_list = list(map(int, input().rstrip().split()))
N_list.sort()

M = int(input().rstrip())
M_list = list(map(int, input().rstrip().split()))

check = {}

for i in N_list :
    if i in check :     # 이미 있으면 1 추가
        check[i] += 1
    else :      # 없으면 1 생성 
        check[i] = 1

for j in M_list :
    if j in check :
        print(check[j], end = " ")
    else :
        print(0, end = " ")