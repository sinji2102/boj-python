import sys

input = sys.stdin.readline

case = int(input())

list_ = list(map(int, input().split()))

M = Y = 0

for i in list_:
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15

if Y > M : 
    print("M", M)
elif Y == M :
    print("Y M", Y)
else:
    print("Y", Y)