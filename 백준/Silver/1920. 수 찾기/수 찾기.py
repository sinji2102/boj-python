import sys
input = sys.stdin.readline

M = int(input().strip())
M_list = set(map(int, input().rstrip().split()))

N = int(input().strip())
N_list = list(map(int, input().rstrip().split()))

for i in N_list :
    if i in M_list :
        print(1)
    else :
        print(0)
