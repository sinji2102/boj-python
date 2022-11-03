import sys
input = sys.stdin.readline

N = int(input().rstrip())

result = 0

for i in range(1, N+1) :
    list_ = list(map(int, str(i)))

    result = i + sum(list_)

    if result == N :
        print(i)
        break

    if i == N:
        print(0)